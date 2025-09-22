import streamlit as st
from summarizer import summarize_text

st.title("Incident Report Summarizer")

text = st.text_area("Enter incident description")

if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        original_length = len(text.strip())
        summary_length = len(summary)
        compression_ratio = summary_length / original_length if original_length > 0 else 0

        st.subheader("Summary")
        st.write(summary)

        st.subheader("Metrics")
        st.write(f"Original length: {original_length} characters")
        st.write(f"Summary length: {summary_length} characters")
        st.write(f"Compression ratio: {compression_ratio:.2f}")
    else:
        st.write("Please enter text")