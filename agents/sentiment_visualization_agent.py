"""
Sentiment Visualization Agent for SteamNoodles
Generates sentiment trend plots from review data over a selected date range.
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Optional

DATA_PATH = "d:/Agent X/data/restaurant_reviews.csv"  # Update with your dataset path


def plot_sentiment_trends(start_date: str, end_date: str, save_path: Optional[str] = None):
    """
    Plots sentiment trends between start_date and end_date (YYYY-MM-DD).
    """
    # Load data
    df = pd.read_csv(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)]

    # Normalize sentiment values
    df['sentiment'] = df['sentiment'].str.strip().str.capitalize()
    # Ensure only expected sentiments
    df = df[df['sentiment'].isin(['Positive', 'Negative', 'Neutral'])]

    # Count sentiments per day
    sentiment_counts = df.groupby([df['timestamp'].dt.date, 'sentiment']).size().unstack(fill_value=0)

    # Ensure all sentiment columns are present
    for col in ['Positive', 'Negative', 'Neutral']:
        if col not in sentiment_counts.columns:
            sentiment_counts[col] = 0
    sentiment_counts = sentiment_counts[['Positive', 'Negative', 'Neutral']]

    # Plot
    sentiment_counts.plot(kind='bar', stacked=False, figsize=(10,6))
    plt.title(f"Sentiment Trends from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()

if __name__ == "__main__":
    # Example usage: expanded date range
    plot_sentiment_trends("2025-08-01", "2025-08-31")
