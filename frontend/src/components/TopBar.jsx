// TopBar — the fixed header at the top of the chat screen.
// Contains the menu icon (opens sidebar), the app logo, and the language switcher.
// The language switcher is a circle showing the current language abbreviation.
// Clicking it opens a small dropdown; selecting a language updates all UI text.
// onMenuClick: called when the hamburger icon is tapped
// language: currently selected language code (e.g. "en")
// onLanguageChange: called with the new language code when the user picks one

import { useState, useRef, useEffect } from "react";
import { LANGUAGES } from "../i18n";
import "./TopBar.css";

// Maps language codes to short uppercase abbreviations shown in the circle
const LANG_ABBR = {
  en: "EN", es: "ES", zh: "ZH", tl: "TL", hi: "HI", ar: "AR",
};

export default function TopBar({ onMenuClick, onLogoClick, language, onLanguageChange }) {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownRef = useRef(null);

  // Close the dropdown if the user clicks anywhere outside it
  useEffect(() => {
    function handleOutsideClick(e) {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setDropdownOpen(false);
      }
    }
    document.addEventListener("mousedown", handleOutsideClick);
    return () => document.removeEventListener("mousedown", handleOutsideClick);
  }, []);

  function handleSelect(code) {
    onLanguageChange(code);
    setDropdownOpen(false);
  }

  return (
    <header className="topbar">
      {/* Hamburger menu — opens the sidebar */}
      <button className="topbar-menu-btn" onClick={onMenuClick} aria-label="Open menu">
        <span className="hamburger-line" />
        <span className="hamburger-line" />
        <span className="hamburger-line" />
      </button>

      {/* App logo — clicking returns to the landing page */}
      <h1 className="topbar-logo" onClick={onLogoClick} role="button" tabIndex={0} onKeyDown={(e) => e.key === "Enter" && onLogoClick?.()}>
        AIdentity
      </h1>

      {/* Language switcher — circle button with current language abbreviation */}
      <div className="lang-switcher" ref={dropdownRef}>
        <button
          className="lang-circle"
          onClick={() => setDropdownOpen((prev) => !prev)}
          aria-label="Select language"
        >
          {LANG_ABBR[language] ?? "EN"}
        </button>

        {/* Dropdown list — appears below the circle when open */}
        {dropdownOpen && (
          <ul className="lang-dropdown">
            {LANGUAGES.map((lang) => (
              <li key={lang.code}>
                <button
                  className={`lang-option ${lang.code === language ? "active" : ""}`}
                  onClick={() => handleSelect(lang.code)}
                >
                  <span className="lang-option-abbr">{LANG_ABBR[lang.code]}</span>
                  <span className="lang-option-label">{lang.label}</span>
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </header>
  );
}
