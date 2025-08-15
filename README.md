# SteamNoodles Automated Restaurant Feedback Agents

**Author:** Thidaya Kaumada Athukorala
**University:** NSBM Green University
**Faculty:** Faculty of Computing
**Year:** 2025

## Project Overview
This repository contains two AI agents for SteamNoodles restaurant feedback automation:

- **Feedback Response Agent:** Automatically replies to customer reviews using sentiment analysis and LLMs.
- **Sentiment Visualization Agent:** Plots sentiment trends over time based on user prompts.

## Setup Instructions
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
4. The synthetic dataset is already included in `data/restaurant_reviews.csv`.
5. Download the official model file for sentiment analysis:
    - Go to the following link: [distilbert-base-uncased-finetuned-sst-2-english/pytorch_model.bin](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english/resolve/main/pytorch_model.bin)
    - Click "Download" to save the file to your computer.
    - Create the directory `models/distilbert-base-uncased-finetuned-sst-2-english/` inside your project folder if it does not exist.
    - Move the downloaded `pytorch_model.bin` file into this directory:
       `models/distilbert-base-uncased-finetuned-sst-2-english/pytorch_model.bin`
    - Your folder structure should look like:
       ```
       Agent-X/
       └── models/
             └── distilbert-base-uncased-finetuned-sst-2-english/
                   └── pytorch_model.bin
       ```
6. (Optional) To generate a new sentiment plot image for your demo:
   ```powershell
   python agents/sentiment_visualization_agent.py --start_date 2025-08-01 --end_date 2025-08-10 --save_path data/sample_sentiment_plot.png
   ```

## How to Test Each Agent
See the `notebooks/demo.ipynb` for sample usage and outputs.

### Feedback Response Agent
Run the following in a Python shell or notebook:
```python
from agents.feedback_response_agent import auto_reply
review = "The food was delicious and the staff were very friendly!"
print(auto_reply(review))
```

### Sentiment Visualization Agent
Generate and display a sentiment plot:
```python
from agents.sentiment_visualization_agent import plot_sentiment_trends
plot_sentiment_trends("2025-08-01", "2025-08-10")
```
Or save the plot as an image:
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

## GitHub Submission Checklist
- [x] All code files in `agents/`
- [x] Synthetic dataset in `data/restaurant_reviews.csv`
- [x] Sample plot image in `data/sample_sentiment_plot.png`
- [x] Demo notebook in `notebooks/demo.ipynb`
- [x] Updated `README.md` with setup, usage, and sample outputs

Upload all code, data, and outputs to your GitHub repository as per instructions.
