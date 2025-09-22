import streamlit as st
from classifier import classify_intent

# Title for the app
st.title("Chatbot Intent Classifier")

# A bit of description
st.write("Enter some text and see what intent it might be!")

# Add some info about the classifier
st.info("This is a simple rule-based classifier. It checks for keywords to identify intents. Rule coverage is about 86% (handles common cases), and accuracy depends on the input.")

# Examples section
with st.expander("Examples of what it can and can't classify"):
    st.write("**What it can handle (should classify correctly):**")
    st.write("- 'Hello there' → greeting")
    st.write("- 'I want to book a table' → booking")
    st.write("- 'There's a problem with my order' → complaint")
    st.write("")
    st.write("**What it might not handle well (classifies as 'unknown'):**")
    st.write("- 'What's the weather like?' → unknown (not in rules)")
    st.write("- 'Tell me a joke' → unknown")
    st.write("- 'Can you help me?' → unknown (too vague)")
    st.write("")
    st.write("Try these to see how it works!")

# Input box for user text
user_text = st.text_input("Your message:", placeholder="Type something like 'Hello' or 'I want to book a table'")

# Button to classify
if st.button("Classify Intent"):
    if user_text.strip():
        # Get the prediction
        intent = classify_intent(user_text)
        # Display result
        st.success(f"Predicted Intent: **{intent}**")
        # Maybe add some fun message
        if intent == 'greeting':
            st.write("Looks like a friendly hello!")
        elif intent == 'booking':
            st.write("Sounds like you want to make a reservation.")
        elif intent == 'complaint':
            st.write("Oh no, seems like there's an issue.")
        else:
            st.write("Hmm, not sure what this is about.")
    else:
        st.error("Please enter some text first.")

# Footer or something
st.write("---")
st.write("Simple rule-based classifier for demo purposes.")