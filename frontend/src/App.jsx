import { useState } from "react";
import LandingPage from "./components/LandingPage";
import TopBar from "./components/TopBar";
import ChatWindow from "./components/ChatWindow";
import InputBar from "./components/InputBar";
import Sidebar from "./components/Sidebar";
import AuthModal from "./components/AuthModal";
import { useChat } from "./hooks/useChat";
import { useChatHistory } from "./hooks/useChatHistory";
import { useLanguage } from "./hooks/useLanguage";
import { useMicrophone } from "./hooks/useMicrophone";
import { t } from "./i18n";
import "./App.css";

export default function App() {
  const [showLanding, setShowLanding] = useState(true);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [authOpen, setAuthOpen] = useState(false);
  const [user, setUser] = useState(null);

  const { language, setLanguage } = useLanguage();
  const { messages, loading, send, reset, restore } = useChat(language);
  const { history, saveChat, deleteChat } = useChatHistory(user?.email);
  const { isRecording, transcript, interimTranscript, start, stop } = useMicrophone(language);

  const hasMessages = messages.length > 0 || loading;

  function handleMicToggle() {
    isRecording ? stop() : start();
  }

  function handleNewChat() {
    if (user && messages.length > 0) saveChat(messages);
    reset();
    setSidebarOpen(false);
  }

  function handleRestoreChat(entry) {
    if (user && messages.length > 0) saveChat(messages);
    restore(entry.messages);
    setSidebarOpen(false);
  }

  function handleStartChat(initialMessage) {
    setShowLanding(false);
    if (initialMessage) send(initialMessage);
  }

  function handleCreateAccount() {
    setShowLanding(false);
    setAuthOpen(true);
  }

  function translate(key) {
    return t(language, key);
  }

  return (
    <div className="app">
      {authOpen && (
        <AuthModal
          onClose={() => setAuthOpen(false)}
          onAuth={(userData) => setUser(userData)}
        />
      )}

      {showLanding ? (
        <LandingPage
          onStartChat={handleStartChat}
          onCreateAccount={handleCreateAccount}
          language={language}
          onLanguageChange={setLanguage}
          isRecording={isRecording}
          transcript={transcript}
          interimTranscript={interimTranscript}
          onMicToggle={handleMicToggle}
        />
      ) : (
        <>
          <Sidebar
            isOpen={sidebarOpen}
            onClose={() => setSidebarOpen(false)}
            onNewChat={handleNewChat}
            user={user}
            history={history}
            onLoginClick={() => { setSidebarOpen(false); setAuthOpen(true); }}
            onLogout={() => { if (messages.length > 0 && user) saveChat(messages); setUser(null); reset(); }}
            onRestoreChat={handleRestoreChat}
            onDeleteChat={deleteChat}
          />

          <TopBar
            onMenuClick={() => setSidebarOpen(true)}
            onLogoClick={() => setShowLanding(true)}
            language={language}
            onLanguageChange={setLanguage}
          />

          {hasMessages ? (
            <>
              <ChatWindow messages={messages} loading={loading} />
              <InputBar
                onSend={send}
                onMicToggle={handleMicToggle}
                isRecording={isRecording}
                transcript={transcript}
                interimTranscript={interimTranscript}
                t={translate}
                centered={false}
              />
            </>
          ) : (
            <div className="empty-state">
              <div className="empty-state-text">
                <p className="empty-title">{translate("emptyTitle")}</p>
                <p className="empty-subtitle">{translate("emptySubtitle")}</p>
              </div>
              <InputBar
                onSend={send}
                onMicToggle={handleMicToggle}
                isRecording={isRecording}
                transcript={transcript}
                interimTranscript={interimTranscript}
                t={translate}
                centered={true}
              />
            </div>
          )}
        </>
      )}
    </div>
  );
}
