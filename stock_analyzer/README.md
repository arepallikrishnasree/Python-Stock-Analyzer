# Stock Price Tracker and Analyzer (Python CLI)

A command-line application built with Python to fetch, analyze, and visualize real-time stock market data.

## Key Features

- **Data Fetching:** Uses the `yfinance` library to download historical stock data (last 6 months) for any specified ticker.
- **Financial Analysis:** Calculates the **50-Day Simple Moving Average (SMA)** for trend analysis.
- **Visualization:** Generates an interactive graph using `matplotlib` showing the closing price and the 50-Day SMA.
- **Libraries:** Built upon the power of `pandas` for efficient data handling.

## How to Run Locally

### 1. Setup

Navigate to the project directory and install the required Python libraries:

```bash
pip install -r requirements.txt