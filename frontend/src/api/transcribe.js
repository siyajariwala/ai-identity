// Sends a recorded audio blob to the backend Whisper endpoint and returns the transcribed text.
// language: BCP-47 code (e.g. "es") — tells Whisper which language to transcribe in
// audioBlob: raw audio from the browser's MediaRecorder API

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export async function transcribeAudio(audioBlob, language = "en") {
  const formData = new FormData();
  formData.append("file", audioBlob, "recording.webm");
  formData.append("language", language);

  const res = await fetch(`${BASE_URL}/api/transcribe`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail ?? `Transcription failed: ${res.status}`);
  }

  const data = await res.json();
  return data.text;
}
