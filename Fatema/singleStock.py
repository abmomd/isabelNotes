import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch stock data
stock = yf.download("ORCL", start="2023-01-01", end="2024-01-01", auto_adjust=True)

# Flatten MultiIndex columns (if needed)
if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

# Use 'Close' instead of 'Adj Close'
stock['Log Returns'] = np.log(stock['Close'] / stock['Close'].shift(1))

print(stock.head())

# Hurst Exponent Calculation
def hurst_exponent(ts, max_lag=20):
    lags = range(2, max_lag)
    tau = [np.sqrt(np.std(ts[lag:] - ts[:-lag])) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0] * 2.0

H = hurst_exponent(stock['Log Returns'].dropna().values)  # Drop NaN values
print(f"Hurst Exponent: {H}")

# Box-Counting Fractal Dimension
def box_counting(ts, scale_range=(2, 50)):
    scales = np.arange(scale_range[0], scale_range[1])
    counts = []
    for scale in scales:
        bins = np.ceil(len(ts) / scale)
        counts.append(len(set(np.floor(ts / scale))))  # Fix calculation
    coeffs = np.polyfit(np.log(scales), np.log(counts), 1)
    return -coeffs[0]

D = box_counting(stock['Close'].values)  # ✅ Use 'Close' instead of 'Adj Close'
print(f"Fractal Dimension: {D}")

# Visualization
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(stock['Close'], label='Stock Price')  # ✅ Use 'Close'
plt.title('Oracle Stock Price')
plt.legend()

plt.subplot(1,2,2)
log_scales = np.log(range(2, 50))
log_counts = np.log([np.std(stock['Close'].values[i:] - stock['Close'].values[:-i]) for i in range(2, 50)])  # ✅ Use 'Close'
sns.regplot(x=log_scales, y=log_counts, scatter=True, label="Hurst Exponent Fit")
plt.xlabel("log(Scale)")
plt.ylabel("log(Standard Deviation)")
plt.legend()
plt.show()
