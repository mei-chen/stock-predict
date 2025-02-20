import yfinance as yf
import pandas as pd
import numpy as np
import talib  # For technical indicators
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import requests

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Define the stock and timeframe
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2023-12-31"

try:
    # Create a session
    session = requests.Session()
    
    # Create a Ticker object with the session
    stock = yf.Ticker(ticker, session=session)
    
    # Force a fresh download by using download instead of history
    df = yf.download(ticker, 
                    start=start_date, 
                    end=end_date,
                    progress=False,
                    session=session)
    
    if df.empty:
        print(f"No data retrieved for {ticker}")
    else:
        print(f"Successfully downloaded {ticker} data")
        print("\nFirst few rows of data:")
        print(df.head())
        print("\nShape of data:", df.shape)

except Exception as e:
    print(f"Error occurred: {str(e)}")
finally:
    session.close()