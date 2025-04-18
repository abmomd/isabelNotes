import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from scipy.stats import linregress

def compute_fluctuation_function(data, scales, q):
    Fq = []
    for s in scales:
        segments = len(data) // s
        F_s = []
        for i in range(segments):
            segment = data[i * s:(i + 1) * s]
            coeffs = np.polyfit(np.arange(s), segment, 1)
            trend = np.polyval(coeffs, np.arange(s))
            fluct = np.sqrt(np.mean((segment - trend) ** 2))
            F_s.append(fluct)
        F_s = np.array(F_s)
        Fq.append(np.mean(F_s ** q) ** (1/q))
    return np.array(Fq)

# Download stock data
ticker = "GOOGL"
df = yf.download(ticker, start="2022-01-01", end="2024-01-01")

# Flatten multi-index columns if necessary
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# Drop NaN values from 'Close' column
df = df.dropna(subset=['Close'])

# Compute log returns
df['Log_Returns'] = np.log(df['Close'] / df['Close'].shift(1)).dropna()

# Define scales and q values
scales = np.logspace(1, 3, num=20, dtype=int)
q_values = np.arange(-5, 6, 1)
Hq = []

for q in q_values:
    Fq = compute_fluctuation_function(df['Log_Returns'].dropna().values, scales, q)
    slope, _, _, _, _ = linregress(np.log(scales), np.log(Fq))
    Hq.append(slope)

Hq = np.array(Hq)
tq = Hq * q - 1

# Plot H(q) vs. q
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(q_values, Hq, marker='o', linestyle='-', color='b')
plt.xlabel("q (Moment order)")
plt.ylabel("H(q) (Hurst Exponent)")
plt.title("H(q) vs. q")
plt.grid()

# Plot t(q) vs. q
plt.subplot(1, 2, 2)
plt.plot(q_values, tq, marker='s', linestyle='-', color='r')
plt.xlabel("q (Moment order)")
plt.ylabel("t(q) (Scaling Exponent)")
plt.title("t(q) vs. q")
plt.grid()

plt.tight_layout()
plt.show()
