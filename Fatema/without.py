import os
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create reports folder if it doesn't exist
if not os.path.exists("reports"):
    os.makedirs("reports")

# List of top 50 stock tickers
top_50_stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "BRK-B", "V", "JNJ",
    "WMT", "JPM", "XOM", "PG", "UNH", "MA", "HD", "CVX", "ABBV", "PFE",
    "COST", "MRK", "PEP", "KO", "TMO", "DIS", "DHR", "ABT", "NFLX", "CSCO",
    "AVGO", "TXN", "NKE", "MCD", "LIN", "VZ", "ADBE", "INTC", "CRM", "HON",
    "PYPL", "AMD", "CMCSA", "ORCL", "IBM", "GE", "AMAT", "SBUX", "CAT", "GS"
]

# Function to fetch and process stock data
def process_stock(ticker):
    stock = yf.download(ticker, start="2023-01-01", end="2024-01-01", auto_adjust=True)

    # Skip if data is empty
    if stock.empty:
        print(f"Skipping {ticker}: No data found")
        return

    # Compute Log Returns
    stock['Log Returns'] = np.log(stock['Close'] / stock['Close'].shift(1))

    # Convert ticker to lowercase and replace special characters for filename
    file_name = ticker.lower().replace("-", "").replace(".", "") + ".png"

    # Plot and save the stock price chart
    plt.figure(figsize=(10, 5))
    plt.plot(stock['Close'], label=f"{ticker} Stock Price", color='blue')
    plt.title(f"{ticker} Stock Price (2023)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    
    # Save the file in the reports folder
    plt.savefig(f"reports/{file_name}")
    plt.close()

    print(f"Saved {ticker} stock chart as reports/{file_name}")

# Run for all top 50 stocks
for stock_ticker in top_50_stocks:
    process_stock(stock_ticker)

print("Processing completed!")
