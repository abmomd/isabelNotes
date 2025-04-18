import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Download stock data
ticker = "GOOGL"
df = yf.download(ticker, start="2023-01-01", end="2024-01-01")

# Flatten multi-index columns if necessary
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# Drop NaN values from 'Close' column
df = df.dropna(subset=['Close'])

# Compute log returns
df['Log_Returns'] = np.log(df['Close'] / df['Close'].shift(1))

# Mock values from your MFDFA output (replace with real computed values if available)
Hq = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])  # Hurst exponent
q = np.arange(-5, 6, 1)  # Moment order
tq = Hq * q - 1  # Multifractal scaling exponent

# Plot H(q) vs. q
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(q, Hq, marker='o', linestyle='-', color='b')
plt.xlabel("q (Moment order)")
plt.ylabel("H(q) (Hurst Exponent)")
plt.title("H(q) vs. q")
plt.grid()

# Plot t(q) vs. q
plt.subplot(1, 2, 2)
plt.plot(q, tq, marker='s', linestyle='-', color='r')
plt.xlabel("q (Moment order)")
plt.ylabel("t(q) (Scaling Exponent)")
plt.title("t(q) vs. q")
plt.grid()

plt.tight_layout()
plt.show()
