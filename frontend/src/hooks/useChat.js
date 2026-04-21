// Manages chat message history and backend communication.
// messages: array of { role: "user" | "assistant", text: string }
// loading: true while waiting for the backend response
// error: holds any error message from a failed request

import { useState } from "react";
import { sendMessage } from "../api/chat";

export function useChat(language) {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function send(question) {
    // Add user message immediately so the UI feels responsive
    setMessages((prev) => [...prev, { role: "user", text: question }]);
    setLoading(true);
    setError(null);

    try {
      const answer = await sendMessage(question, language);
      setMessages((prev) => [...prev, { role: "assistant", text: answer }]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  // Clears the conversation without reloading the page
  function reset() {
    setMessages([]);
    setLoading(false);
    setError(null);
  }

  return { messages, loading, error, send, reset };
}
