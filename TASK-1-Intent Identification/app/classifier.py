# This is the classifier module for intent identification
# It uses simple rules based on keywords

def classify_intent(user_input):
    # Convert to lowercase for case-insensitive matching
    text = user_input.lower()

    # Check for greeting keywords
    if any(word in text for word in ['hello', 'hi', 'hey', 'good morning']):
        return 'greeting'

    # Check for booking keywords
    elif any(word in text for word in ['book', 'reserve', 'schedule', 'appointment']):
        return 'booking'

    # Check for complaint keywords
    elif any(word in text for word in ['problem', 'issue', 'complaint', 'bad']):
        return 'complaint'

    # If none match, it's unknown
    else:
        return 'unknown'

# Maybe add some helper functions later if needed