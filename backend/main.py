import os
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from groq import Groq
from pydantic import BaseModel, Field

from backend.bay_area_resources import (
    BAY_AREA_LEGAL_AID_ORGS,
    LEGAL_AID_DISCLAIMER,
    LegalAidOrganization,
)
from backend.checklists import (
    ChecklistItem,
    DISCLAIMER as CHECKLIST_DISCLAIMER,
    VisaType,
    get_checklist,
)
from backend.prompts import IMMIGRATION_ASSISTANT_SYSTEM_PROMPT

load_dotenv()

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


def _groq_client() -> Groq:
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not set. Add it to a .env file in the project root.",
        )
    return Groq(api_key=key)


def _optional_rag_context(question: str) -> str | None:
    try:
        from rag.retrieve import retrieve_context

        ctx = retrieve_context(question)
        return ctx if ctx and ctx.strip() else None
    except Exception:
        return None


app = FastAPI(
    title="AI-Identity",
    description=(
        "**CSC 603/803 capstone** — API for **AI-Identity**, a **Bay Area–focused**, "
        "multilingual **U.S. immigration** assistant (plain-language guidance on forms and "
        "processes; **not** legal advice). "
        "Target languages: **English, Spanish, Mandarin, Tagalog, Hindi, Arabic**. "
        "Form scope (MVP): **I-765**, **I-485**, **I-821D**. "
        "This is **not** a medical app. "
        "**POST /api/chat** is the main endpoint; set `use_rag` when Chroma retrieval is populated. "
        "**POST /checklist** returns a curated document checklist by visa/status code. "
        "**GET /resources** lists Bay Area nonprofit legal aid organizations."
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=8000)
    language: str | None = Field(
        default=None,
        description=(
            "Optional language code so the model answers in that language "
            "(proposal target set: en, es, zh, tl, hi, ar). "
            "If omitted, the assistant follows the language of `question`."
        ),
    )
    use_rag: bool = Field(
        default=False,
        description="If true, inject retrieved USCIS-oriented chunk context when ChromaDB is available.",
    )


class ChatResponse(BaseModel):
    answer: str
    model: str


class ChecklistRequest(BaseModel):
    visa_type: VisaType = Field(
        ...,
        description="Machine-readable visa/status path; see OpenAPI enum for valid values.",
    )


class ChecklistResponse(BaseModel):
    visa_type: VisaType
    display_name: str
    summary: str
    items: list[ChecklistItem]
    disclaimer: str


class ResourcesResponse(BaseModel):
    organizations: list[LegalAidOrganization]
    count: int
    disclaimer: str


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    """Browser default URL has no handler otherwise; send people to the API docs."""
    return RedirectResponse(url="/docs")


@app.get(
    "/health",
    tags=["System"],
    summary="Is the API running?",
    description="DevOps-style check that the server responds. Unrelated to medical health or USCIS medical exams.",
)
def health() -> dict[str, Literal["ok"]]:
    return {"status": "ok"}


@app.post(
    "/checklist",
    response_model=ChecklistResponse,
    tags=["Immigration assistant"],
    summary="Personalized document checklist",
    description=(
        "Returns a curated checklist of commonly required documents for the selected visa/status path. "
        "Educational only—not legal advice; users should verify against official USCIS instructions."
    ),
)
def checklist(body: ChecklistRequest) -> ChecklistResponse:
    bundle = get_checklist(body.visa_type)
    return ChecklistResponse(
        visa_type=bundle.visa_type,
        display_name=bundle.display_name,
        summary=bundle.summary,
        items=bundle.items,
        disclaimer=CHECKLIST_DISCLAIMER,
    )


@app.get(
    "/resources",
    response_model=ResourcesResponse,
    tags=["Immigration assistant"],
    summary="Bay Area legal aid organizations",
    description=(
        "Free and low-cost nonprofit legal aid organizations serving the San Francisco Bay Area. "
        "Verify intake hours and eligibility on each organization's website."
    ),
)
def resources() -> ResourcesResponse:
    orgs = BAY_AREA_LEGAL_AID_ORGS
    return ResourcesResponse(
        organizations=orgs,
        count=len(orgs),
        disclaimer=LEGAL_AID_DISCLAIMER,
    )


@app.post(
    "/api/chat",
    response_model=ChatResponse,
    tags=["Immigration assistant"],
    summary="Ask the immigration assistant",
)
def chat(body: ChatRequest) -> ChatResponse:
    client = _groq_client()

    user_content = body.question.strip()
    if body.language:
        user_content = (
            f"{user_content}\n\n(Reply in language code: {body.language}.)"
        )

    messages: list[dict[str, str]] = [
        {"role": "system", "content": IMMIGRATION_ASSISTANT_SYSTEM_PROMPT},
    ]

    if body.use_rag:
        context = _optional_rag_context(body.question)
        if context:
            messages.append(
                {
                    "role": "system",
                    "content": "Use the following excerpts from official-style instructions as grounding. "
                    "If they conflict with the user's situation or seem incomplete, say so and do not over-claim.\n\n"
                    f"{context}",
                }
            )

    messages.append({"role": "user", "content": user_content})

    try:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
            temperature=0.3,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e)) from e

    answer = completion.choices[0].message.content
    if not answer:
        raise HTTPException(status_code=502, detail="Empty model response")

    return ChatResponse(answer=answer.strip(), model=completion.model)


class TranscribeResponse(BaseModel):
    text: str


@app.post(
    "/api/transcribe",
    response_model=TranscribeResponse,
    tags=["Immigration assistant"],
    summary="Transcribe spoken audio to text",
)
async def transcribe(
    file: UploadFile = File(..., description="Audio file recorded in the browser (webm/mp4/wav)"),
    language: str = Form(default="en", description="BCP-47 language code to guide Whisper transcription"),
) -> TranscribeResponse:
    # Read the raw audio bytes from the uploaded file
    audio_bytes = await file.read()
    if not audio_bytes:
        raise HTTPException(status_code=400, detail="Audio file is empty.")

    client = _groq_client()

    try:
        # Send audio to Groq's Whisper endpoint for transcription
        # The filename extension hints at the format; webm is what browsers produce by default
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=(file.filename or "recording.webm", audio_bytes),
            language=language,
            response_format="text",
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e)) from e

    return TranscribeResponse(text=transcription.strip())


# Run from repo root: uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
