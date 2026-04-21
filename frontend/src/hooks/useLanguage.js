// Manages the selected language across the app.
// Returns the current language code and a setter to change it.
// Defaults to English on first load.

import { useState } from "react";

export function useLanguage() {
  const [language, setLanguage] = useState("en");
  return { language, setLanguage };
}
