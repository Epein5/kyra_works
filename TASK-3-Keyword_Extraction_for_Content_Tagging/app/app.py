import streamlit as st
from keyword_tagger import extract_keywords

# App title
st.title("Keyword Extraction for Content Tagging")

# Description
st.write("Paste some text and get automatically extracted keywords. Uses NLTK for frequency-based extraction.")

# Text input
user_text = st.text_area("Enter your content here:", height=150, placeholder="Type or paste a paragraph...")

# Button to extract
if st.button("Extract Keywords"):
    if user_text.strip():
        # Extract keywords
        keywords = extract_keywords(user_text)
        st.success("Keywords extracted!")
        st.write("**Text Preview:**", user_text[:200] + "...")
        st.write("**Extracted Keywords:**", ", ".join(keywords))
    else:
        st.error("Please enter some text.")

# Footer
st.write("---")
st.write("Automatic extraction demo using NLTK.")