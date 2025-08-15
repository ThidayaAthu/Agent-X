"""
Feedback Response Agent for SteamNoodles
Automatically analyzes sentiment and generates polite replies to customer feedback using HuggingFace Transformers (local model).
"""
from transformers import pipeline
from typing import Tuple

# Load sentiment analysis pipeline from local directory
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="d:/Agent X/models/distilbert-base-uncased-finetuned-sst-2-english",
    tokenizer="d:/Agent X/models/distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(review: str) -> str:
    """
    Uses HuggingFace to classify sentiment as positive, negative, or neutral.
    """
    result = sentiment_analyzer(review)[0]
    label = result["label"].lower()
    if "positive" in label:
        return "Positive"
    elif "negative" in label:
        return "Negative"
    else:
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
    Main function: takes review, returns sentiment and auto-reply.
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
