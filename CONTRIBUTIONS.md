# Kataliya Sungkamee — Technical Contributions

**Role:** Frontend, Backend API, Voice Integration  
**Project:** AI-Identity — Multilingual U.S. Immigration Assistant  
**Branch:** `kataliya-dev`

---

## Overview

I built the FastAPI backend from scratch (chat and transcription endpoints), authored the immigration assistant system prompt, and implemented the entire React frontend — including the chat UI, language switcher, voice input, and i18n setup across all six supported languages.

---

## What I Built

### Backend API (`backend/main.py`)

Designed and implemented the full FastAPI application:

- **`POST /api/chat`** — accepts a question, optional language code, and `use_rag` flag. Builds a message list with the system prompt, optionally injects ChromaDB-retrieved USCIS context, calls the Groq LLM (`llama-3.3-70b-versatile`), and returns a typed response.
- **`POST /api/transcribe`** — accepts a browser-recorded audio file (webm/mp4/wav), sends it to Groq's Whisper large-v3 endpoint with a BCP-47 language hint, and returns the transcript text. Enables fully voice-driven conversations.
- **`GET /health`** — lightweight liveness check for DevOps monitoring.
- **CORS middleware** — configurable via `CORS_ORIGINS` env variable for flexible local and production setups.
- **Optional RAG injection** — `_optional_rag_context()` wraps the ChromaDB retrieval call so the API degrades gracefully when the vector store isn't populated, without erroring.

### Immigration Assistant System Prompt (`backend/prompts.py`)

Authored the system instructions that define the assistant's behavior:
- Enforces plain-language, step-by-step guidance using official USCIS terminology
- Explicit non-legal-advice guardrails with escalation language for high-stakes cases
- Instructs the model to reply in whatever language the user writes in, or switch on explicit request
- Calibrated tone: patient, non-alarmist, honest about uncertainty

### Frontend Application (`frontend/src/`)

Initialized the React + Vite project and built the full UI:

**Components:**
- `SplashScreen` — landing/intro screen
- `ChatWindow` — conversation thread rendering
- `MessageBubble` — per-message display with role-aware styling
- `InputBar` — text input with send action
- `TopBar` — app header with language switcher
- `Sidebar` — navigation panel

**Hooks:**
- `useChat.js` — manages conversation state, sends messages to `/api/chat`, handles loading and error states
- `useMicrophone.js` — handles browser microphone access, audio recording, and posts audio to `/api/transcribe` for voice input
- `useLanguage.js` — manages active language selection across the app

**API clients:**
- `api/chat.js` — typed wrapper around `POST /api/chat`
- `api/transcribe.js` — typed wrapper around `POST /api/transcribe`

**i18n (`frontend/src/i18n/`):**

Set up `i18next` with translation files for all six target languages:
- `en.js` · `es.js` · `zh.js` · `tl.js` · `hi.js` · `ar.js`

This allows the UI itself (labels, placeholders, buttons) to switch language independently of the AI response language.

---

## Technical Decisions

- **Groq for both LLM and Whisper** — unified API client, fast inference, and the same key for both chat and transcription keeps the backend simple with no extra service dependencies
- **Graceful RAG degradation** — wrapped the ChromaDB call in a try/except so the chat endpoint works in isolation before the vector store is populated; RAG is opt-in via `use_rag: true`
- **BCP-47 language hint on transcription** — passing the user's selected language to Whisper improves accuracy for accented speech in non-English languages, which is critical given the target user base
- **i18n on the frontend** — separating UI language from AI response language means a Tagalog speaker can have the interface in Tagalog while the AI answers based on what they type, without coupling the two

---

## Commits

Authored under `katsaliya <kataliyaschool@gmail.com>` on `kataliya-dev`:
- `Initialized Vite, frontend structure, translation files, and index.js`
- `Improved chat UX, layout, and i18n support`
- `Updated backend/main.py, handles audio files, transcribe api`
