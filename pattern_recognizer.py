def find_candle_patterns(df):
    # ক্যান্ডেলস্টিক প্যাটার্ন ডিটেকশন
    last = df.iloc[-1]
    prev = df.iloc[-2]
    
    if last['Close'] > prev['Open'] and last['Open'] < prev['Close']:
        return "BULLISH ENGULFING 🟢"
    elif last['Close'] < prev['Open'] and last['Open'] > prev['Close']:
        return "BEARISH ENGULFING 🔴"
    return "Scanning Patterns..."
