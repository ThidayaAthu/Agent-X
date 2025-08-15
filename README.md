
# SteamNoodles Automated Restaurant Feedback Agents

**Author:** Thidaya Kaumada Athukorala  
**University:** NSBM Green University  
**Year:** 2025

## Project Summary
This project implements a multi-agent system for automating restaurant feedback analysis and visualization. The approach uses two Python agents:

- **Feedback Response Agent:** Uses HuggingFace Transformers (DistilBERT) for sentiment analysis and generates polite, context-aware replies to customer reviews. The model runs locally for privacy and reliability.
- **Sentiment Visualization Agent:** Loads a synthetic dataset of restaurant reviews, normalizes sentiment values, and plots sentiment trends over time using pandas and matplotlib. The agent ensures all sentiment types are visualized and handles missing data gracefully.

## How to Test Both Agents

### Setup
1. Clone this repository.
2. Create and activate a Python virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the official model file for sentiment analysis:
   - [distilbert-base-uncased-finetuned-sst-2-english/pytorch_model.bin](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english/resolve/main/pytorch_model.bin)
   - Place it in the `models/distilbert-base-uncased-finetuned-sst-2-english/` directory.
5. The synthetic dataset is already included in `data/restaurant_reviews.csv`.

### Test the Feedback Response Agent
Run the following in a Python shell or notebook:
```python
from agents.feedback_response_agent import auto_reply
review = "The food was delicious and the staff were very friendly!"
review, sentiment, reply = auto_reply(review)
print(f"Review: {review}")
print(f"Sentiment: {sentiment}")
print(f"Auto-reply: {reply}")
```

### Test the Sentiment Visualization Agent
Generate and display a sentiment plot:
```python
from agents.sentiment_visualization_agent import plot_sentiment_trends
plot_sentiment_trends("2025-08-01", "2025-08-10")
```
Or save the plot as an image:
```python
plot_sentiment_trends("2025-08-01", "2025-08-10", save_path="data/sample_sentiment_plot.png")
```

*** End Patch
```python
plot_sentiment_trends("2025-08-01", "2025-08-10", save_path="data/sample_sentiment_plot.png")
```

## Sample Prompts & Expected Outputs
**Auto-response for a sample feedback:**
```
Review: The food was delicious and the staff were very friendly!
Agent Reply: Thank you for your positive feedback! We're delighted you enjoyed the food and our friendly staff. We look forward to serving you again soon!
```

**Sentiment plot for a selected date range:**
See `data/sample_sentiment_plot.png` for a sample output image.

## Dataset
- [Kaggle Restaurant Reviews Dataset](https://www.kaggle.com/datasets)

## Submission
- [x] All code files in `agents/`
- [x] Synthetic dataset in `data/restaurant_reviews.csv`
- [x] Sample plot image in `data/sample_sentiment_plot.png`
- [x] Demo notebook in `notebooks/demo.ipynb`
- [x] Updated `README.md` with setup, usage, and sample outputs

Upload all code, data, and outputs to your GitHub repository as per instructions.
