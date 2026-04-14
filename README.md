# 📊 Financial News Summarizer

An AI-powered web app that instantly summarizes financial articles and earnings reports using Google Gemini. Paste any article and get a structured breakdown: TL;DR, key takeaways, notable figures, and market sentiment.

---

## Screenshot

> _Add a screenshot here once the app is running. In Streamlit, take one with Cmd+Shift+4 on Mac._

![App screenshot](assets/screenshot.png)

---

## Live Demo

> _Add your Streamlit Cloud URL here after deploying._

[▶ Try it live](https://your-app-name.streamlit.app)

---

## Local Setup (Mac)

Follow these steps exactly — no prior experience needed.

### 1. Prerequisites

Make sure you have Python 3.11+ installed. Check with:

```bash
python3 --version
```

If not installed, download it from [python.org](https://www.python.org/downloads/).

### 2. Clone or download the project

```bash
cd ~/Desktop          # or wherever you want the project to live
git clone https://github.com/your-username/financial-summarizer.git
cd financial-summarizer
```

### 3. Create and activate a virtual environment

A virtual environment keeps project dependencies isolated.

```bash
python3 -m venv venv
source venv/bin/activate
```

Your terminal prompt will now show `(venv)` — that means it worked.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Get a free Gemini API key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API key** and copy it

### 6. Set up your API key

```bash
cp .env.example .env
```

Open `.env` in any text editor (e.g. TextEdit, VS Code) and replace `your_gemini_api_key_here` with your real key:

```
GEMINI_API_KEY=AIza...your_actual_key...
```

### 7. Run the app

```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`. Paste an article and click **Summarize**!

---

## Deploying to Streamlit Cloud (optional)

1. Push this project to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in
3. Click **New app** → select your repo and `app.py`
4. Go to **Settings → Secrets** and add:
   ```
   GEMINI_API_KEY = "your_key_here"
   ```
5. Click **Deploy** — your live URL will appear in a minute

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | Web UI framework — no HTML/CSS needed |
| [Google Gemini](https://ai.google.dev) | Large language model for summarization |
| [google-generativeai](https://pypi.org/project/google-generativeai/) | Official Python SDK for Gemini |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Loads `.env` API keys for local development |
| Python 3.11+ | Programming language |

---

## What I Learned

Building this project taught me:

- **How to call an AI API** — sending a text prompt to Gemini and receiving a structured response using the `google-generativeai` SDK.
- **Prompt engineering** — writing a clear, specific prompt that reliably returns Markdown with exactly the sections I wanted.
- **Streamlit fundamentals** — building an interactive web app with `st.text_area`, `st.button`, `st.markdown`, and spinner/error states — all in pure Python with no frontend knowledge required.
- **API key security** — using `.env` files locally and `st.secrets` on the cloud so keys are never hardcoded or committed to Git.
- **Graceful error handling** — what to show users when the key is missing, the input is empty, or the API call fails.
- **Virtual environments** — isolating project dependencies with `venv` so they don't conflict with other projects on the same machine.

---

## Project Structure

```
01-financial-summarizer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies with pinned versions
├── .env.example        # Template — copy to .env and add your key
├── .env                # Your real API key (git-ignored)
├── .gitignore          # Files excluded from version control
└── README.md           # This file
```
