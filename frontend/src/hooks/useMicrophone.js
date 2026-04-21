// Handles browser microphone recording and transcription via the backend Whisper endpoint.
// isRecording: true while the mic is active
// transcript: the transcribed text returned from the backend
// start: begins recording
// stop: stops recording and sends audio to /api/transcribe

import { useState, useRef } from "react";
import { transcribeAudio } from "../api/transcribe";

export function useMicrophone(language) {
  const [isRecording, setIsRecording] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [error, setError] = useState(null);
  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);

  async function start() {
    setError(null);
    setTranscript("");

    // Request mic permission from the browser
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorderRef.current = mediaRecorder;
    chunksRef.current = [];

    mediaRecorder.ondataavailable = (e) => chunksRef.current.push(e.data);

    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(chunksRef.current, { type: "audio/webm" });
      // Stop all mic tracks to release the browser mic indicator
      stream.getTracks().forEach((track) => track.stop());
      try {
        const text = await transcribeAudio(audioBlob, language);
        setTranscript(text);
      } catch (err) {
        setError(err.message);
      }
    };

    mediaRecorder.start();
    setIsRecording(true);
  }

  function stop() {
    mediaRecorderRef.current?.stop();
    setIsRecording(false);
  }

  return { isRecording, transcript, error, start, stop };
}
