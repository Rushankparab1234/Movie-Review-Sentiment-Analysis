import re
import string
import joblib
import streamlit as st

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# Load Model

model = joblib.load("models/sentiment_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


# NLP Objects

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


# Text Cleaning Function

def clean_text(text):

    text = text.lower()

    text = re.sub(r"<.*?>", "", text)

    text = re.sub(r"http\\S+|www\\S+", "", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = re.sub(r"\d+", "", text)

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)



# Prediction Function

def predict_sentiment(review):

    cleaned = clean_text(review)

    vector = tfidf.transform([cleaned])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    if prediction == 1:
        sentiment = "Positive 😊"
        confidence = probability[1]
    else:
        sentiment = "Negative 😞"
        confidence = probability[0]

    return sentiment, confidence



# Streamlit UI

st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Analysis")

st.write(
    """
    This application predicts whether a movie review is **Positive** or **Negative**
    using **Natural Language Processing (NLP)** and **Machine Learning**.
    """
)

review = st.text_area(
    "Enter your movie review:",
    height=200
)

if st.button("Predict Sentiment"):

    if review.strip() == "":

        st.warning("Please enter a review.")

    else:

        sentiment, confidence = predict_sentiment(review)

        if "Positive" in sentiment:
            st.success(f"Prediction: {sentiment}")
        else:
            st.error(f"Prediction: {sentiment}")

        st.info(f"Confidence: {confidence*100:.2f}%")