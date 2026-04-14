"""
Financial News Summarizer
Uses Google Gemini to summarize financial articles and earnings reports.
"""

import streamlit as st
import google.generativeai as genai
import os

# Load environment variables from .env file when running locally.
# This won't cause errors if the file doesn't exist (e.g., on Streamlit Cloud).
from dotenv import load_dotenv
load_dotenv()


# ── Page configuration ────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Financial News Summarizer",
    page_icon="📊",
    layout="centered",
)


# ── Helper: load the Gemini API key ──────────────────────────────────────────

def get_api_key() -> str | None:
    """
    Returns the Gemini API key.

    Priority:
      1. GEMINI_API_KEY environment variable  (local .env file)
      2. st.secrets["GEMINI_API_KEY"]          (Streamlit Cloud secrets)
    """
    # Try the environment variable first (set by python-dotenv from .env)
    key = os.getenv("GEMINI_API_KEY")
    if key:
        return key

    # Fall back to Streamlit Cloud secrets
    try:
        return st.secrets["GEMINI_API_KEY"]
    except (FileNotFoundError, KeyError):
        return None


# ── Helper: call Gemini and return the summary ────────────────────────────────

def summarize_article(article_text: str, api_key: str) -> str:
    """
    Sends the article to Gemini and returns a structured markdown summary.
    """
    # Configure the SDK with our API key
    genai.configure(api_key=api_key)

    # Select the model
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Craft a clear, structured prompt
    prompt = f"""You are a financial analyst assistant. Analyze the following financial article or earnings report and provide a structured response in Markdown format with exactly these four sections:

## TL;DR
Write a clear, plain-English summary in exactly 3 sentences.

## Key Takeaways
Provide exactly 5 bullet points highlighting the most important facts.

## Notable Financial Figures
Extract and list key numbers mentioned (e.g., revenue, EPS, guidance, growth percentages). If a figure is not mentioned, write "Not mentioned".

## Overall Sentiment
State one word — **Bullish**, **Bearish**, or **Neutral** — followed by a single sentence explaining why.

---

Here is the article to analyze:

\"\"\"
{article_text}
\"\"\"
"""

    response = model.generate_content(prompt)
    return response.text


# ── UI ────────────────────────────────────────────────────────────────────────

st.title("📊 Financial News Summarizer")
st.markdown(
    "Paste any financial article, earnings report, or press release below "
    "and get an instant AI-powered summary — including key figures and market sentiment."
)
st.divider()

# Large text area for user input
article_input = st.text_area(
    label="Paste your financial article here",
    placeholder="e.g. Apple reported quarterly revenue of $94.9 billion...",
    height=300,
)

# Summarize button
if st.button("✨ Summarize", use_container_width=True, type="primary"):

    # ── Validation: check for empty input ────────────────────────────────────
    if not article_input.strip():
        st.warning("Please paste some text before clicking Summarize.")
        st.stop()

    # ── Validation: check for API key ────────────────────────────────────────
    api_key = get_api_key()
    if not api_key:
        st.error(
            "**API key not found.** \n\n"
            "- **Local:** Create a `.env` file in this folder with `GEMINI_API_KEY=your_key_here`\n"
            "- **Streamlit Cloud:** Add `GEMINI_API_KEY` to your app's Secrets settings."
        )
        st.stop()

    # ── Call the API ──────────────────────────────────────────────────────────
    with st.spinner("Analyzing article with Gemini..."):
        try:
            summary = summarize_article(article_input, api_key)
        except Exception as e:
            # Surface a friendly error message without exposing internals
            st.error(f"**Something went wrong while calling the Gemini API:**\n\n`{e}`")
            st.stop()

    # ── Display the result ────────────────────────────────────────────────────
    st.success("Summary ready!")
    st.markdown(summary)

    # Optional: let the user download the summary as a text file
    st.download_button(
        label="⬇️ Download summary",
        data=summary,
        file_name="financial_summary.md",
        mime="text/markdown",
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Powered by [Google Gemini](https://ai.google.dev) · Built with [Streamlit](https://streamlit.io)")
