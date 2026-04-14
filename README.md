# AI-Identity

**CSC 603 / CSC 803 — Generative AI Capstone**  
Free, multilingual, AI-powered assistant for Bay Area immigrants navigating U.S. visa forms, deadlines, and USCIS processes.

---

## Team

| Name              | Email               |
| ----------------- | ------------------- |
| Fayeeza Shaikh    | fshaikh5@sfsu.edu   |
| Siya Jariwala     | sjariwala1@sfsu.edu |
| Kataliya Sungkamee | ksungkamee@sfsu.edu |

---

## 1. Project title

**AI-Identity**

---

## 2. Problem statement

Navigating the U.S. immigration system is one of the most confusing bureaucratic experiences anyone can face—and for non-English speakers, it is especially hard to do alone. Federal forms such as the **I-485** (adjustment of status) and **I-765** (work authorization) are long, dense with legal language, and unforgiving: one misunderstood question can contribute to delays, denials, or serious downstream issues.

Most official tools and sites are **English-first**. Private immigration attorneys often cost roughly **$150–$300 per hour**, which is out of reach for many families. Community legal aid is under-resourced, with long waitlists. Millions of people therefore navigate a **high-stakes system** with limited reliable support.

This is acute in the **Bay Area**, one of the most linguistically diverse regions in the U.S., with a large foreign-born population and dozens of languages in daily use—including **Spanish, Mandarin, Tagalog, Hindi, and Arabic** among the most widely spoken—yet there is no widely accessible, multilingual, AI-guided way to understand forms and next steps in **the user’s own language**.

**AI-Identity** addresses that gap: a **free** assistant that explains complex forms in plain terms, supports **multilingual** Q&A, will support **personalized checklists** and **curated local legal resources**, and is designed for **mobile-friendly** use.

---

## 3. Objectives

1. Build a **multilingual AI assistant** supporting **English, Spanish, Mandarin, Tagalog, Hindi, and Arabic**—languages central to Bay Area immigrant communities.
2. Help users receive **plain-language answers** to immigration questions **quickly** (target: responsive guidance without making users hunt across many government pages for basic orientation).
3. Provide **field-by-field walkthroughs** of at least **three major USCIS forms** (**I-765**, **I-485**, and **I-821D**), explaining questions in context and flagging common mistakes.
4. Generate a **personalized immigration checklist** based on visa type, current status, and goals—covering required forms, supporting documents, fees, and deadlines (as the product matures).
5. Surface a **curated set** of **verified free legal aid** resources relevant to the **Bay Area**, matched where possible to **language** and **case type**.
6. **Evaluate** the platform through **user testing** with **10–15** immigrant participants (course proposal); MVP testing may start smaller and scale up—measuring clarity, usefulness, and user confidence **before and after** using the tool.

---

## 4. Project description

- **Idea:** AI-Identity helps Bay Area immigrants navigate visa forms, deadlines, and processes **in their preferred language**, with cautious, plain-language explanations—not legal advice.
- **Final product (target):** A **mobile-friendly web application** where users **type** (and later **speak**) questions, receive **step-by-step guidance**, a **downloadable checklist**, and pointers to **nearby free legal aid** resources.
- **Generative AI use:** **Multimodal** direction—**text** for form Q&A, walkthroughs, and checklist generation; **audio** for **voice input/output** (speech-to-text and spoken responses) as the voice layer is integrated.

---

## 5. Technical approach

**Architecture (capstone plan)**

- **Models / APIs:** Large language model for reasoning and responses; **speech-to-text** for voice questions; translation / multilingual support for output (exact vendor choices may evolve during implementation; see **repository status** below).
- **Frameworks:** **React** (frontend), **FastAPI** (backend), **LangChain + ChromaDB** (RAG over public USCIS-oriented materials and curated aid references).
- **Training:** **Pre-trained models only**—no fine-tuning required for the MVP.
- **Data:** **Public** USCIS.gov materials and **public** Bay Area legal aid directories—**no collection or storage of personal user data** as a design goal for the MVP.

**Repository status (what exists in *this* codebase today)**

- **Backend:** **FastAPI** with `POST /api/chat` and optional **RAG** context injection (`use_rag`) when Chroma retrieval is available.
- **LLM layer (current):** **Groq** API for chat completions (used in development and integration; course milestones may specify this explicitly).
- **RAG:** **ChromaDB** + Python ingestion/retrieval scripts under `rag/` (e.g. I-765–oriented content pipeline—expand toward I-485 / I-821D and policy manual excerpts per proposal).
- **Frontend:** `frontend/` placeholder—**React** UI, language switcher, and **Whisper**-style voice input are **planned** per proposal timeline.
- **LangChain:** described in the proposal as part of the RAG approach; **not required** yet for the minimal RAG path in-repo—can be introduced as orchestration grows.

---

## 6. Team roles and responsibilities

- **Person 1 — Frontend and voice interface (lead: Kataliya)**  
  Build the user-facing **React** app: **chat UI**, **language switcher**, **mobile-friendly** layout, and integration of **voice input** (speech-to-text) so users can speak questions, with **text input always available** as fallback.

- **Person 2 — Data and RAG pipeline (lead: Siya)**  
  Build the **knowledge base**: collect/scrape **public** USCIS and Bay Area legal aid materials, **chunk** documents, store embeddings in **ChromaDB**, retrieve relevant chunks at query time, connect RAG to the **FastAPI** backend, and keep refresh/re-scrape paths documented.

- **Person 3 — AI logic and prompt engineering (lead: Fayeeza)**  
  Own what the model **says and how it behaves**: LLM integration, **system prompts** and **form walkthrough** prompts, **checklist** generation behavior (once product flows are wired), and **quality tuning** across supported languages—with strong disclaimers (not a lawyer; verify on official USCIS sources).

All three collaborate on **testing**, **integration**, **debugging**, and the **final presentation**—the split above is **lead ownership**, not isolation.

---

## 7. Expected outcomes

**Deliverables:** Live demo, codebase, slide deck, short demo video.

**Success metrics (targets from the proposal)**

- AI answers immigration questions usefully in **at least five** supported languages (stretch: all six).
- Form walkthrough flows operate **without errors** for **I-765** and **I-485** in the demo path.
- User testing with **3–5** real non-English speakers yields **positive usability** feedback (with a path to expand toward **10–15** participants).
- Typical **response time under ~5 seconds** per query under normal conditions.

---

## 8. Timeline (9 weeks)

| Week | Milestone |
| ---- | --------- |
| 1 | Proposal approved—finalize scope, GitHub repo, roles, API keys |
| 2 | Research and data collection—USCIS sources and Bay Area legal aid references |
| 3 | RAG pipeline—chunk documents, ChromaDB, basic retrieval tests |
| 4 | Core AI logic—LLM integration, walkthrough prompts, checklist generator |
| 5 | Frontend—React UI, language switcher, voice input |
| 6 | Full integration—frontend ↔ backend, end-to-end testing |
| 7 | User testing with multilingual users, bug fixes, accuracy improvements |
| 8 | Final polish, slide deck, demo video |
| 9 | Final presentation |

---

## 9. Potential challenges and mitigations

- **Translation accuracy:** legal terms can mistranslate—**mitigation:** verify key immigration vocabulary per language; keep official English terms where precision matters.
- **USCIS content changes:** pages and fees update—**mitigation:** versioned sources and a documented **re-ingestion / refresh** cadence (e.g. monthly checks).
- **Voice with accented speech:** ASR may fail for some users—**mitigation:** **text input always available**.
- **Scope creep:** immigration is huge—**mitigation:** cap MVP to **three forms** and **six languages** as listed above; document everything else as future work.

---

## 10. References

- Migration Policy Institute. *Immigration data for the San Francisco–Oakland–Berkeley metro area.* [MPI Data Hub — California](https://www.migrationpolicy.org/data/state-profiles/state/demographics/CA)
- U.S. Citizenship and Immigration Services. *Forms and filing.* [uscis.gov/forms](https://www.uscis.gov/forms)
- U.S. Citizenship and Immigration Services. *Check case processing times.* [egov.uscis.gov/processing-times](https://egov.uscis.gov/processing-times)
- U.S. Citizenship and Immigration Services. *Policy manual.* [uscis.gov/policy-manual](https://www.uscis.gov/policy-manual)
- Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS 2020.
- Westermann, H., et al. (2023). *Using Large Language Models to Support Legal Decision-Making.* *Artificial Intelligence and Law.*
- Stanford Legal Design Lab. *Legal Navigator.* [legalnav.org](https://legalnav.org)
- National Immigration Law Center. *Know your rights resources.* [nilc.org](https://www.nilc.org)

---

## Run the API locally

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Put your Groq API key in .env as GROQ_API_KEY=...
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` for interactive docs (`/` redirects there). Chat: **`POST /api/chat`**.
