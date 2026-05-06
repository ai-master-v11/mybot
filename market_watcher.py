import yfinance as yf

def fetch_live_feed(ticker="EURUSD=X"):
    # লাইভ ডাটা কানেক্টর
    feed = yf.download(ticker, period="1d", interval="1m")
    return feed
