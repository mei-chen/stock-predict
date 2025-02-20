from datetime import datetime as dt

import pytz
import streamlit as st
import yfinance as yf

tz = pytz.timezone("America/New_York")
start = tz.localize(dt(2013,1,1))
end = tz.localize(dt.today())

tickers = "MA,V,AMZN,JPM,BA".split(",")
df = yf.download(tickers,start, end, auto_adjust=True)['Close']

st.table(df.head())