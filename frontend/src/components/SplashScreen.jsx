// SplashScreen — shown once when the app first loads.
// Fades the "AIdentity" logo in, holds it, then fades it out.
// Calls onFinish() when the animation is done so App.jsx can switch to the chat screen.

import { useEffect, useState } from "react";
import "./SplashScreen.css";

export default function SplashScreen({ onFinish }) {
  // Controls which phase of the animation we're in: "in", "hold", or "out"
  const [phase, setPhase] = useState("in");

  useEffect(() => {
    // Fade in for 800ms
    const holdTimer = setTimeout(() => setPhase("hold"), 800);
    // Hold for 1.5s after fade-in
    const outTimer = setTimeout(() => setPhase("out"), 2300);
    // Tell App.jsx we're done after fade-out completes
    const doneTimer = setTimeout(() => onFinish(), 3100);

    return () => {
      clearTimeout(holdTimer);
      clearTimeout(outTimer);
      clearTimeout(doneTimer);
    };
  }, [onFinish]);

  return (
    <div className={`splash ${phase}`}>
      <h1 className="splash-logo">AIdentity</h1>
    </div>
  );
}
