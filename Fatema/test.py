
import yfinance as yf

# Fetch data
stock = yf.download("GOOGL", start="2023-01-01", end="2024-01-01")

# Print available columns
print("Columns in DataFrame:", stock.columns)

