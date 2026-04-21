// Sends the user's question to the backend and returns the AI's answer.
// language: BCP-47 code (e.g. "es") — tells the AI which language to reply in
// useRag: if true, the backend will search the PDF form chunks for extra context

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export async function sendMessage(question, language = "en", useRag = false) {
  const res = await fetch(`${BASE_URL}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, language, use_rag: useRag }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail ?? `Request failed: ${res.status}`);
  }

  const data = await res.json();
  return data.answer;
}
