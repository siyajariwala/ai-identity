import "./Sidebar.css";

function formatDate(ts) {
  const d = new Date(ts);
  const now = new Date();
  const diffDays = Math.floor((now - d) / 86400000);
  if (diffDays === 0) return "Today";
  if (diffDays === 1) return "Yesterday";
  if (diffDays < 7) return `${diffDays} days ago`;
  return d.toLocaleDateString(undefined, { month: "short", day: "numeric" });
}

export default function Sidebar({ isOpen, onClose, onNewChat, user, history = [], onLoginClick, onLogout, onRestoreChat, onDeleteChat, isLanding = false }) {
  return (
    <>
      {isOpen && <div className="sidebar-overlay" onClick={onClose} />}

      <nav className={`sidebar ${isOpen ? "open" : ""}`}>
        <button className="sidebar-close" onClick={onClose} aria-label="Close menu">
          ✕
        </button>

        {!isLanding && (
          <>
            <button className="sidebar-new-chat" onClick={onNewChat}>
              + New Chat
            </button>
            <hr className="sidebar-divider" />
          </>
        )}

        {isLanding ? (
          <div className="sidebar-landing-auth">
            <div className="sidebar-auth-btns">
              <button className="sidebar-btn-login"  onClick={onLoginClick}>Log In</button>
              <button className="sidebar-btn-signup" onClick={onLoginClick}>Sign Up</button>
            </div>
            <p className="sidebar-save-cta">
              Creating an account lets you save your chat history and pick up exactly where you left off.
            </p>
          </div>
        ) : user ? (
          <>
            <div className="sidebar-user">
              <div className="sidebar-avatar">{user.name.charAt(0).toUpperCase()}</div>
              <div className="sidebar-user-info">
                <span className="sidebar-user-name">{user.name}</span>
                <span className="sidebar-user-email">{user.email}</span>
              </div>
              <button className="sidebar-logout" onClick={onLogout} title="Log out">↩</button>
            </div>

            <div className="sidebar-history">
              {history.length === 0 ? (
                <p className="sidebar-history-empty">Your saved chats will appear here.</p>
              ) : (
                history.map((entry) => (
                  <div key={entry.id} className="sidebar-history-item" onClick={() => onRestoreChat(entry)}>
                    <div className="sidebar-history-title">{entry.title}</div>
                    <div className="sidebar-history-meta">{formatDate(entry.savedAt)}</div>
                    <button
                      className="sidebar-history-delete"
                      title="Delete"
                      onClick={(e) => { e.stopPropagation(); onDeleteChat(entry.id); }}
                    >
                      ✕
                    </button>
                  </div>
                ))
              )}
            </div>
          </>
        ) : (
          <div className="sidebar-auth">
            <span className="sidebar-lock">🔒</span>
            <p>Save your conversations by signing in</p>
            <div className="sidebar-auth-btns">
              <button className="sidebar-btn-login" onClick={onLoginClick}>Log In</button>
              <button className="sidebar-btn-signup" onClick={onLoginClick}>Sign Up</button>
            </div>
          </div>
        )}
      </nav>
    </>
  );
}
