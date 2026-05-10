// InputBar — the message input area.
// When centered=true (empty state): sits inline below the prompt, not fixed to the bottom.
// When centered=false (chatting): fixed to the bottom of the screen.
// onSend: called with the message string when the user submits
// onMicToggle: called when the mic button is tapped
// isRecording: true while the mic is active (changes mic button appearance)
// transcript: text returned from Whisper — auto-fills the input when it arrives
// t: translation function for placeholder text

import { useState } from "react";
import "./InputBar.css";

export default function InputBar({ onSend, onMicToggle, isRecording, transcript, t, centered }) {
  const [text, setText] = useState("");
  const [lastTranscript, setLastTranscript] = useState("");

  // When Whisper returns a new transcript, populate the input automatically.
  if (transcript && transcript !== lastTranscript) {
    setLastTranscript(transcript);
    setText(transcript);
  }

  function handleSend() {
    const trimmed = text.trim();
    if (!trimmed) return;
    onSend(trimmed);
    setText("");
  }

  // Allow sending with the Enter key (Shift+Enter adds a new line)
  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  return (
    // centered class removes fixed positioning so the bar flows with the empty state layout
    <div className={`input-bar ${centered ? "centered" : ""}`}>
      {/* Text input — grows with content up to a max height */}
      <textarea
        className="input-field"
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={t("placeholder")}
        rows={1}
      />

      {/* Mic button — turns active/filled while recording */}
      <button
        className={`input-btn mic-btn ${isRecording ? "recording" : ""}`}
        onClick={onMicToggle}
        aria-label={isRecording ? "Stop recording" : "Start recording"}
      >
        🎙️
      </button>

      {/* Send button — disabled when input is empty */}
      <button
        className="input-btn send-btn"
        onClick={handleSend}
        aria-label="Send message"
        disabled={!text.trim()}
      >
        ➤
      </button>
    </div>
  );
}
