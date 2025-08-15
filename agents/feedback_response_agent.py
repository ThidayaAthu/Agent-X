"""
Feedback Response Agent for SteamNoodles
Automatically analyzes sentiment and generates polite replies to customer feedback using HuggingFace Transformers (local model).

Author: Thidaya Kaumada Athukorala
University: NSBM Green University
Faculty: Faculty of Computing
Year: 2025
"""
from transformers import pipeline
from typing import Tuple

# Load sentiment analysis pipeline from local directory
import os
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'distilbert-base-uncased-finetuned-sst-2-english'))
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

def analyze_sentiment(review: str) -> str:
    """
    Uses HuggingFace to classify sentiment as positive, negative, or neutral.
    Returns 'Neutral' if review is empty or invalid.
    """
    if not isinstance(review, str) or not review.strip():
        return "Neutral"
    try:
        result = sentiment_analyzer(review)[0]
        label = result["label"].lower()
        if "positive" in label:
            return "Positive"
        elif "negative" in label:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "Neutral"

def generate_reply(review: str, sentiment: str) -> str:
    """
    Generates a polite, context-aware reply based on sentiment and review text.
    """
    if sentiment == "Positive":
        return "Thank you for your wonderful feedback! We're delighted you enjoyed your experience."
    elif sentiment == "Negative":
        return "We're sorry to hear about your experience. We appreciate your feedback and will work to improve."
    else:
        return "Thank you for sharing your thoughts. We value all feedback and hope to serve you even better next time."

def auto_reply(review: str) -> Tuple[str, str, str]:
    """
    Main function: takes review, returns (review, sentiment, auto-reply).
    Handles empty or invalid input gracefully.
    """
    sentiment = analyze_sentiment(review)
    reply = generate_reply(review, sentiment)
    return review, sentiment, reply

if __name__ == "__main__":
    # Example usage
    sample_review = "The noodles were delicious, but the service was a bit slow."
    review, sentiment, reply = auto_reply(sample_review)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print(f"Auto-reply: {reply}")
