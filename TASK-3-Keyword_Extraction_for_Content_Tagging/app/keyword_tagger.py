import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

# Download data if needed
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

def extract_keywords(text, num_keywords=5):
    # Simple keyword extraction using frequency
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stopwords.words('english')]
    word_freq = Counter(words)
    keywords = [word for word, _ in word_freq.most_common(num_keywords)]
    return keywords