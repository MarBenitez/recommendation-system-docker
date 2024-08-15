# app/sentiment_analysis.py
from models.ber_model_hf import predict_sentiment

def analyze_sentiment(review):
    """Analyze the sentiment of a given review text."""
    sentiment = predict_sentiment(review)
    return sentiment
