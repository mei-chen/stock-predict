import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set seed for reproducibility
np.random.seed(42)

# Generate a toy dataset with 1,000 samples
num_samples = 1000

df = pd.DataFrame({
    "Open": np.random.uniform(100, 500, num_samples),  # Random stock opening price
    "High": np.random.uniform(100, 500, num_samples),  # Random high price
    "Low": np.random.uniform(100, 500, num_samples),   # Random low price
    "Close": np.random.uniform(100, 500, num_samples), # Random closing price
    "Volume": np.random.randint(1000, 50000, num_samples),  # Random volume
})

# Target Variable: 1 if Close > Open (Price increased), 0 otherwise
df["Target"] = (df["Close"] > df["Open"]).astype(int)

# Show first few rows
print(df.head())