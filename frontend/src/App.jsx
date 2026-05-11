// App.jsx — root component that wires everything together.
// Manages top-level state: splash screen, sidebar open/close, language selection.
// Passes the right props and callbacks down to each component.

import { useState } from "react";
import SplashScreen from "./components/SplashScreen";
import TopBar from "./components/TopBar";
import ChatWindow from "./components/ChatWindow";
import InputBar from "./components/InputBar";
import Sidebar from "./components/Sidebar";
import { useChat } from "./hooks/useChat";
import { useLanguage } from "./hooks/useLanguage";
import { useMicrophone } from "./hooks/useMicrophone";
import { t } from "./i18n";
import "./App.css";

export default function App() {
  // Show splash screen on first load only — new chat does NOT re-trigger this
  const [showSplash, setShowSplash] = useState(true);

  // Sidebar open/close state
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Language selection — shared across chat, mic, and UI text
  const { language, setLanguage } = useLanguage();

  // Chat state, send function, and reset for new conversations
  const { messages, loading, send, reset } = useChat(language);

  // Microphone recording and Whisper transcription
  const { isRecording, transcript, interimTranscript, start, stop } = useMicrophone(language);

  const hasMessages = messages.length > 0 || loading;

  // Toggle mic: start if idle, stop if already recording
  function handleMicToggle() {
    isRecording ? stop() : start();
  }

  // Clear the conversation without reloading — splash screen does not show again
  function handleNewChat() {
    reset();
    setSidebarOpen(false);
  }

  // Translate helper pre-bound to the current language
  function translate(key) {
    return t(language, key);
  }

  if (showSplash) {
    return <SplashScreen onFinish={() => setShowSplash(false)} />;
  }

  return (
    <div className="app">
      <Sidebar
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        onNewChat={handleNewChat}
      />

      <TopBar
        onMenuClick={() => setSidebarOpen(true)}
        language={language}
        onLanguageChange={setLanguage}
      />

      {/* When no messages: show centered empty state with input bar below the prompt.
          When chatting: show the scrollable message thread instead. */}
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
    </div>
  );
}
