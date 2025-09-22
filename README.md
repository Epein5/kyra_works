# kyra_works

A collection of small NLP apps built with Streamlit. Implemented tasks include intent identification, keyword extraction, incident report summarization, and sentiment analysis.

Note on scope: Tasks 2 and 4 were not NLP-related in the original assignment, so they were intentionally skipped as instructed.

## Quick start

1) Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Run any task app (examples below). Streamlit will open in your browser.

---

## Task 1 — Intent Identification

- Path: `TASK-1-Intent_Identification/app/app.py`
- What it does: Classifies a short user message into simple intents using a rule-based keyword matcher.
- Intents covered: `greeting`, `booking`, `complaint`, or `unknown`.
- How it works: See `classifier.py` for the keyword rules; it performs lowercase matching on predefined keywords.

Run it:

```bash
streamlit run TASK-1-Intent_Identification/app/app.py
```

Example inputs:
- "Hello there" → greeting
- "I want to book a table" → booking
- "There's a problem with my order" → complaint
- Anything outside the rules → unknown

---

## Task 3 — Keyword Extraction for Content Tagging

- Path: `TASK-3-Keyword_Extraction_for_Content_Tagging/app/app.py`
- What it does: Extracts top keywords from a paragraph using NLTK tokenization, stopword removal, and simple frequency counts.
- How it works: `keyword_tagger.py` tokenizes text, removes punctuation and English stopwords, counts token frequencies, and returns the top `n` tokens (default 5).

Run it:

```bash
streamlit run TASK-3-Keyword_Extraction_for_Content_Tagging/app/app.py
```

Input: Paste one or more paragraphs.
Output: List of extracted keywords, plus a short text preview.

---

## Task 5 — Text Summarization for Incident Reports

- Path: `TASK-5-Text_Summarization_for_Incident_Reports/app/app.py`
- What it does: Generates an extractive summary of an incident description and shows simple metrics.
- How it works: Uses the Sumy implementation of LexRank (`summarizer.py`) to select representative sentences. Default summary length is 3 sentences.

Run it:

```bash
streamlit run TASK-5-Text_Summarization_for_Incident_Reports/app/app.py
```

Input: Paste an incident description.
Output: Summary text and metrics (original length, summary length, compression ratio).

---

## Task 6 — Sentiment Analysis

- Path: `TASK-6-Sentiment_Analysis/app/app.py`
- What it does: Performs sentiment analysis on user feedback using NLTK VADER. Accepts either a CSV upload or manual multiline text input.
- How it works: Computes VADER compound scores and labels each entry as `Positive`, `Negative`, or `Neutral`. Displays a results table and charts (bar, pie, histogram).

Run it:

```bash
streamlit run TASK-6-Sentiment_Analysis/app/app.py
```

Inputs:
- CSV upload: The first column is assumed to contain the feedback text (header optional). Non-empty rows are used.
- Manual input: Enter one feedback item per line in the textarea.

Outputs:
- A table with each feedback, its label, and the compound score
- Distribution visualizations (bar chart, pie chart, histogram)

---

## Skipped tasks

- Task 2 and Task 4 were not NLP-related; they were skipped per instructions from the reviewers.

---

## Notes and troubleshooting

- NLTK data: The apps download required NLTK resources on first run (e.g., `vader_lexicon`, `stopwords`, tokenizers). If your environment has no internet access, pre-download these resources where possible.
- CSV parsing (Task 6): The app reads the first column for text. Ensure the first column contains the feedback strings; empty rows are ignored.
- Port conflicts: If Streamlit’s default port is busy, you can specify a port, e.g.:

```bash
streamlit run TASK-6-Sentiment_Analysis/app/app.py --server.port 8502
```

---

## Repository layout

```
TASK-1-Intent_Identification/
	app/
		app.py
		classifier.py

TASK-3-Keyword_Extraction_for_Content_Tagging/
	app/
		app.py
		keyword_tagger.py

TASK-5-Text_Summarization_for_Incident_Reports/
	app/
		app.py
		summarizer.py

TASK-6-Sentiment_Analysis/
	app/
		app.py

requirements.txt
```

If you need additional automation (e.g., a combined launcher or Docker setup), open an issue and we can add it.

REadme generate by ai ..

