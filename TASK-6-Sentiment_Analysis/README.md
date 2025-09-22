# Sentiment Analysis Task

This project demonstrates sentiment analysis on user feedback using Python.

## What We Did

- **Notebook (test.ipynb)**: Contains test cases with sample feedback texts. Performs sentiment analysis using NLTK's VADER and visualizes the distribution with a bar chart.

- **Streamlit App (app/app.py)**: A web app where users can upload a CSV file with feedback or enter texts manually. It analyzes sentiments, shows results in a table, and displays multiple charts: bar chart, pie chart (side by side), and a histogram of sentiment scores.

## Requirements

- Python 3.x
- Libraries: streamlit, pandas, nltk, matplotlib

Install dependencies: `pip install -r requirements.txt`

## Running the App

Navigate to the `app` folder and run: `streamlit run app.py`

## Deployment

The app is deployed and accessible at: https://kyra-sentimental-analysis.streamlit.app/

## Running the Notebook

Open `test.ipynb` in Jupyter and run the cells.