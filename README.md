# ARCANOVA AI 📖🎙️

> **The Ultimate Local Interactive Storytelling & Kokoro TTS Voice Narration Suite**

![Palette](https://img.shields.io/badge/Theme-Black%20%7C%20Soft%20Beige%20%7C%20White-E6D7C3?style=for-the-badge)
![Model](https://img.shields.io/badge/LLM-Qwen%202.5%203B-informational?style=for-the-badge)
![TTS](https://img.shields.io/badge/Voice-Kokoro%20TTS%2082M-success?style=for-the-badge)

**ARCANOVA AI** seamlessly integrates the **Qwen 2.5 3B LLM** and **Kokoro TTS (82M)** inside a bespoke Streamlit interface styled in an ultra-luxurious **Obsidian Black, Soft Beige, and White** color palette.

---

## ✨ Features

- **📖 Story & Narration in One Touch**: Generate complete stories and full audio narration simultaneously with a single click.
- **👥 Audience Section Pockets**:
  - **Teenagers Pocket**: High-octane Cyberpunk, Magic Academy, Space Quest, and Dystopian Resistance.
  - **Adults Pocket**: Sophisticated Psychological Thrillers, Philosophical Sci-Fi, Dark Noir, and Historical Mysteries.
- **🎙️ Speech & Dictation Input Access**: Dictate or type story prompts directly in the interface.
- **🎨 Custom Black/Beige/White Design**: Bespoke CSS featuring Google Fonts (*Cormorant Garamond* & *Plus Jakarta Sans*), glowing audio players, and black placeholder inputs.
- **✨ Complete Story & Warm Endings**: Guaranteed sentence completion and beautiful closing inspirational messages.
- **💻 100% Local Inference**: Runs locally without requiring Hugging Face gated API keys.

---

## 🚀 Quick Start (Local Browser)

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/your-username/arcanova-ai.git
cd arcanova-ai
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Download Models Locally
```bash
python download_models.py
```

### 3. Launch Application in Browser
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser!

---

## 🛠️ Building Standalone Windows Executable (.EXE)

To bundle ARCANOVA AI into a standalone software `.exe` application for Windows:

```bash
python build_exe.py
```

The compiled standalone executable directory will be generated inside `dist/ARCANOVA_AI/`.

---

## 📁 Repository Structure

```
arcanova-ai/
├── app.py                  # Main Streamlit application
├── download_models.py      # Automated model caching script
├── build_exe.py           # PyInstaller build setup
├── run_app.py              # Launcher script for EXE bundle
├── requirements.txt        # Python dependencies
├── .gitignore              # Git exclusion rules
├── README.md               # Repository documentation
└── src/
    ├── config.py           # Global constants & theme tokens
    ├── styles.py           # Custom CSS styling system
    ├── audience_pockets.py # Teenagers & Adults genre prompts
    ├── llm_engine.py       # Qwen 2.5 3B local engine loader
    └── tts_engine.py       # Kokoro TTS audio narration synthesizer
```

---

## 📄 License
Released under the MIT License.
