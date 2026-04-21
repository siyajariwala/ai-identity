// ChatWindow — the scrollable message thread in the middle of the screen.
// Shows an empty state prompt when there are no messages yet.
// Automatically scrolls to the latest message as new ones come in.
// messages: array of { role: "user" | "assistant", text: string }
// loading: true while waiting for the AI response (shows a typing indicator)

import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";
import "./ChatWindow.css";

export default function ChatWindow({ messages, loading }) {
  // Used to scroll to the bottom whenever messages update
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <main className="chat-window">
      {/* Empty state — shown before the first message is sent */}
      {messages.length === 0 && !loading && (
        <div className="chat-empty">
          <p>Start a conversation</p>
          <p>Ask me anything about your immigration form</p>
        </div>
      )}

      {/* Message thread */}
      {messages.map((msg, i) => (
        <MessageBubble key={i} role={msg.role} text={msg.text} />
      ))}

      {/* Typing indicator — shown while the AI is generating a response */}
      {loading && (
        <div className="bubble-wrapper assistant">
          <div className="bubble typing-indicator">
            <span /><span /><span />
          </div>
        </div>
      )}

      {/* Invisible anchor element to scroll into view */}
      <div ref={bottomRef} />
    </main>
  );
}
