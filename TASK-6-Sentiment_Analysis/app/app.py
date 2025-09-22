import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

# Download VADER if needed
nltk.download('vader_lexicon', quiet=True)

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

st.title("Sentiment Analysis on User Feedback")

st.write("Upload a CSV file with feedback texts or enter feedback texts below.")

# Option to upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Option to input text
text_input = st.text_area("Or enter feedback texts (one per line)")

feedbacks = []

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Assume the first column contains the feedback texts
    feedback_column = df.columns[0]
    feedbacks = df[feedback_column].dropna().tolist()
    st.write(f"Loaded {len(feedbacks)} feedbacks from CSV.")

elif text_input:
    feedbacks = [line.strip() for line in text_input.split('\n') if line.strip()]
    st.write(f"Entered {len(feedbacks)} feedbacks.")

if feedbacks:
    # Analyze sentiments
    sentiments = []
    results = []
    for feedback in feedbacks:
        score = sia.polarity_scores(feedback)
        compound = score['compound']
        if compound >= 0.05:
            sentiment = 'Positive'
        elif compound <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        sentiments.append(sentiment)
        results.append({'Feedback': feedback, 'Sentiment': sentiment, 'Score': compound})

    # Display results
    st.subheader("Sentiment Analysis Results")
    results_df = pd.DataFrame(results)
    st.dataframe(results_df)

    # Sentiment distribution
    sentiment_counts = Counter(sentiments)
    st.subheader("Sentiment Distribution")
    st.bar_chart(pd.DataFrame.from_dict(sentiment_counts, orient='index'))

else:
    st.write("Please upload a CSV or enter some feedback texts to analyze.")