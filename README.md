# AI-Identity

Free, multilingual AI assistant for Bay Area immigrants navigating U.S. immigration forms and processes.

> **CSC 603 / CSC 803 — Generative AI Capstone · San Francisco State University**

---

## What It Does

AI-Identity lets users ask plain-language questions about U.S. immigration forms in their own language and get clear, step-by-step guidance back — without needing to pay an attorney for basic orientation.

Supported languages: **English · Spanish · Mandarin · Tagalog · Hindi · Arabic**  
Form coverage (MVP): **I-765** (work authorization) · **I-485** (adjustment of status) · **I-821D** (DACA)

---

## Architecture

```
┌─────────────────────────────────────────────┐
│           Frontend (React + Vite)           │
│  Chat UI · Language switcher · Voice input  │
└────────────────────┬────────────────────────┘
                     │ HTTP
┌────────────────────▼────────────────────────┐
│           Backend (FastAPI + Python)         │
│  POST /api/chat · POST /api/transcribe       │
│  Groq LLM (llama-3.3-70b) + Whisper v3      │
└──────────────┬──────────────────────────────┘
               │ optional
┌──────────────▼──────────────────────────────┐
│         RAG Pipeline (ChromaDB)             │
│  USCIS docs · Bay Area legal aid references │
└─────────────────────────────────────────────┘
```

---

## Running Locally

**Backend:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your Groq API key to .env: GROQ_API_KEY=...
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` for the interactive API explorer.

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## Tech Stack

| Layer | Tech |
|---|---|
| Frontend | React 19, Vite, i18next (6 languages) |
| Backend | Python, FastAPI |
| LLM | Groq API — llama-3.3-70b-versatile |
| Speech-to-Text | Groq Whisper large-v3 |
| Vector DB | ChromaDB |
| RAG | LangChain + custom ingestion scripts |

---

## Team

| Name | Role |
|---|---|
| Kataliya Sungkamee | Frontend, backend API, voice integration |
| Siya Jariwala | Data pipeline, RAG, ChromaDB |
| Fayeeza Shaikh | AI logic, prompt engineering |

> This is not legal advice. Always verify information on the official [USCIS website](https://www.uscis.gov).
