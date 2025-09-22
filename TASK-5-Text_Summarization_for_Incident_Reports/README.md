# Text Summarization for Incident Reports

This is a simple Streamlit web app that summarizes incident report texts using extractive summarization. It helps quickly identify key events and outcomes from long descriptions.

## Features
- Input incident descriptions via text area.
- Generates a concise summary using the LexRank algorithm.
- Displays original length, summary length, and compression ratio.

## How to Run Locally
1. Install dependencies: `pip install streamlit sumy nltk`.
2. Run the app: `streamlit run app/app.py`.

## Deployment
The app is deployed at: https://kyra-summarization.streamlit.app/

## Files
- `app/app.py`: Main Streamlit app.
- `app/summarizer.py`: Summarization logic.
- `test.ipynb`: Jupyter notebook for testing with sample incidents.