// MessageBubble — renders a single message in the chat thread.
// role: "user" or "assistant" — determines alignment and bubble style
// text: the message content

import "./MessageBubble.css";

export default function MessageBubble({ role, text }) {
  return (
    // Wrapper aligns the bubble left (assistant) or right (user)
    <div className={`bubble-wrapper ${role}`}>
      <div className="bubble">
        {text}
      </div>
    </div>
  );
}
