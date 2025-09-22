import streamlit as st
from summarizer import summarize_text

st.title("Incident Report Summarizer")

text = st.text_area("Enter incident description")

if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        st.write("Summary:", summary)
    else:
        st.write("Please enter text")