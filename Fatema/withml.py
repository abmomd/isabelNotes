import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Download stock data
stock = yf.download('GOOGL', start='2023-01-01', end='2024-01-01', interval='1d')
stock['Log Returns'] = np.log(stock['Close'] / stock['Close'].shift(1))

# Drop initial NaNs from Log Returns
stock.dropna(inplace=True)

# Hurst Exponent Calculation
def hurst_exponent(ts, max_lag=20):
    if len(ts) < 5: return np.nan  # Ensure enough data points
    lags = range(2, max_lag)
    tau = [np.sqrt(np.std(ts[lag:] - ts[:-lag])) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0] * 2.0

# Box-Counting Fractal Dimension
def box_counting(ts, scale_range=(2, 50)):
    if len(ts) < 5: return np.nan  # Ensure enough data points
    scales = np.arange(scale_range[0], scale_range[1])
    counts = []
    for scale in scales:
        bins = np.ceil(len(ts) / scale)
        counts.append(len(set(np.floor(ts / scale))))  # Fixed set error
    coeffs = np.polyfit(np.log(scales), np.log(counts), 1)
    return -coeffs[0]



# Ensure 'Hurst' is calculated correctly
stock['Hurst'] = stock['Log Returns'].rolling(window=100, min_periods=10).apply(hurst_exponent, raw=True)

# Ensure 'Fractal_Dim' is calculated correctly
stock['Fractal_Dim'] = stock['Close'].rolling(window=100, min_periods=10).apply(box_counting, raw=True)

# Debugging print
print("Missing Values Before Drop:\n", stock[['Hurst', 'Fractal_Dim']].isna().sum())

import pandas as pd

# ✅ Step 1: Flatten MultiIndex Columns
stock.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in stock.columns]
print("\n🔄 Flattened Column Names:", stock.columns.tolist())

# ✅ Step 2: Update Expected Column Names
expected_columns = ['Hurst_', 'Fractal_Dim_']  # Notice the added "_"

# ✅ Step 3: Check if columns exist
missing_columns = [col for col in expected_columns if col not in stock.columns]
if missing_columns:
    print(f"\n❌ ERROR: Missing columns: {missing_columns}")
    print(f"✔️ Available Columns: {stock.columns.tolist()}")
else:
    print("\n✅ 'Hurst_' and 'Fractal_Dim_' exist in DataFrame.")

# ✅ Step 4: Convert to numeric (to avoid dtype issues)
for col in expected_columns:
    stock[col] = pd.to_numeric(stock[col], errors='coerce')

# ✅ Step 5: Drop NaN values safely
try:
    stock.dropna(subset=expected_columns, inplace=True)
    print("\n✅ Successfully dropped missing values!")
except KeyError as e:
    print(f"\n❌ KeyError: {e}")
    print("✔️ Double-check column names using `stock.columns.tolist()`")

# ✅ Step 6: Print final shape
print("\n📏 DataFrame Shape After Drop:", stock.shape)


# Try dropping NaN values again
stock.dropna(subset=['Hurst_', 'Fractal_Dim_'], inplace=True)
print("✅ NaN values dropped successfully.")


# Debug after dropping NaNs
print("Rows after Drop:", len(stock))

# Define Features and Target
features = stock[['Hurst_', 'Fractal_Dim_']]
# Shift target column
stock['Target'] = stock['Close_GOOGL'].shift(-1)

# Drop NaN rows after shifting
stock.dropna(subset=['Target'], inplace=True)

# Now extract features (X) and target (y)
X = stock.drop(columns=['Target'])  # Features
y = stock['Target']                 # Target variable

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Visualization
plt.plot(y_test.values, label="Actual Prices")
plt.plot(predictions, label="Predicted Prices", linestyle='dashed', color = 'red')
plt.legend()
plt.title("Stock Price Prediction using Fractal Features")
plt.show()

# Model Performance
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")
