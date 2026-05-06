def project_07_indicator(df):
    # কাস্টম মেমেটাম এবং সাইকোলজি ইনডেক্স
    df['Momentum'] = df['Close'] - df['Close'].shift(4)
    if df['Momentum'].iloc[-1] > 0:
        return "STRONG BULLISH"
    return "STRONG BEARISH"
