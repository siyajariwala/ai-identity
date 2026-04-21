// Sidebar — slides in from the left when the hamburger menu is tapped.
// Shows a "New Chat" button and a placeholder for past conversations (requires account).
// isOpen: controls whether the sidebar is visible
// onClose: called when the X button or the overlay is tapped
// onNewChat: called when the user starts a new conversation

import "./Sidebar.css";

export default function Sidebar({ isOpen, onClose, onNewChat }) {
  return (
    <>
      {/* Dark overlay behind the sidebar — tap to close */}
      {isOpen && <div className="sidebar-overlay" onClick={onClose} />}

      <nav className={`sidebar ${isOpen ? "open" : ""}`}>
        {/* Close button */}
        <button className="sidebar-close" onClick={onClose} aria-label="Close menu">
          ✕
        </button>

        {/* New chat button — clears the current conversation */}
        <button className="sidebar-new-chat" onClick={() => { onNewChat(); onClose(); }}>
          + New Chat
        </button>

        <hr className="sidebar-divider" />

        {/* Placeholder — shown until account/auth feature is built */}
        <div className="sidebar-placeholder">
          <span className="sidebar-lock">🔒</span>
          <p>Create an account to save your conversations</p>
        </div>
      </nav>
    </>
  );
}
