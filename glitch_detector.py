def find_market_glitch(df):
    # ক্যান্ডেলের মাঝখানের গ্যাপ বা অস্বাভাবিক জাম্প ধরা
    last_close = df['Close'].iloc[-1]
    last_open = df['Open'].iloc[-1]
    
    body_size = abs(last_close - last_open)
    if body_size > (df['High'] - df['Low']).mean() * 3:
        return "GLITCH DETECTED ⚡", "Manipulation Warning"
    return "Smooth Market", "No Glitch"
