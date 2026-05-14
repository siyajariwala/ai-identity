import { useState, useEffect } from "react";

function storageKey(email) {
  return `chat_history_${email}`;
}

function load(email) {
  if (!email) return [];
  try {
    return JSON.parse(localStorage.getItem(storageKey(email)) || "[]");
  } catch {
    return [];
  }
}

function save(email, chats) {
  localStorage.setItem(storageKey(email), JSON.stringify(chats));
}

// Returns a short title derived from the first user message in the conversation.
function summarize(messages) {
  const first = messages.find((m) => m.role === "user");
  if (!first) return "Untitled conversation";
  const text = first.text.trim();
  return text.length <= 60 ? text : text.slice(0, 57) + "…";
}

export function useChatHistory(userEmail) {
  const [history, setHistory] = useState(() => load(userEmail));

  // Reload history whenever the logged-in user changes.
  useEffect(() => {
    setHistory(load(userEmail));
  }, [userEmail]);

  function saveChat(messages) {
    if (!userEmail || messages.length === 0) return;
    const entry = {
      id: Date.now(),
      title: summarize(messages),
      messages,
      savedAt: Date.now(),
    };
    setHistory((prev) => {
      const updated = [entry, ...prev];
      save(userEmail, updated);
      return updated;
    });
  }

  function deleteChat(id) {
    setHistory((prev) => {
      const updated = prev.filter((c) => c.id !== id);
      save(userEmail, updated);
      return updated;
    });
  }

  function clearAll() {
    setHistory([]);
    if (userEmail) localStorage.removeItem(storageKey(userEmail));
  }

  return { history, saveChat, deleteChat, clearAll };
}
