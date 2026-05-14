import { useEffect, useState } from "react";
import "./SplashScreen.css";

const SUBTITLES = [
  "Understand your immigration documents, in your language",
  "Entiende tus documentos de inmigración, en tu idioma",
  "用您的语言了解您的移民文件",
  "Unawain ang iyong mga dokumento sa imigrasyon, sa iyong wika",
  "अपनी भाषा में अपने इमिग्रेशन दस्तावेज़ समझें",
  "افهم وثائق الهجرة الخاصة بك، بلغتك",
];

const HOLD_MS = 600;    // fade-in duration
const PER_LANG_MS = 480; // time each language is shown
const FADE_OUT_MS = 800;

export default function SplashScreen({ onFinish }) {
  const [phase, setPhase] = useState("in");
  const [langIndex, setLangIndex] = useState(0);

  useEffect(() => {
    const timers = [];

    timers.push(setTimeout(() => setPhase("hold"), HOLD_MS));

    // Cycle through languages after hold
    SUBTITLES.forEach((_, i) => {
      if (i > 0) {
        timers.push(setTimeout(() => setLangIndex(i), HOLD_MS + i * PER_LANG_MS));
      }
    });

    const totalCycle = HOLD_MS + SUBTITLES.length * PER_LANG_MS;
    timers.push(setTimeout(() => setPhase("out"), totalCycle));
    timers.push(setTimeout(() => onFinish(), totalCycle + FADE_OUT_MS));

    return () => timers.forEach(clearTimeout);
  }, [onFinish]);

  return (
    <div className={`splash ${phase}`}>
      <div className="splash-content">
        <h1 className="splash-logo">AIdentity</h1>
        <p key={langIndex} className="splash-subtitle">
          {SUBTITLES[langIndex]}
        </p>
      </div>
    </div>
  );
}
