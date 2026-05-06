import yfinance as yf
import pandas as pd

def fetch_live_feed(ticker="EURUSD=X"):
    try:
        # গত ১ দিনের ১ মিনিটের ডাটা নিয়ে আসা
        data = yf.download(ticker, period="1d", interval="1m", progress=False)
        
        if data is not None and not data.empty:
            # ডাটা পরিষ্কার করা যেন এরর না আসে
            return data
        else:
            return pd.DataFrame()
    except Exception as e:
        print(f"Data Fetch Error: {e}")
        return pd.DataFrame()
