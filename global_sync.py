from datetime import datetime
import pytz

def get_market_sessions():
    # লন্ডন ও নিউ ইয়র্ক সেশনের সময় চেক করা
    utc_now = datetime.now(pytz.utc)
    if 8 <= utc_now.hour <= 16:
        return "LONDON SESSION - High Volatility"
    elif 13 <= utc_now.hour <= 21:
        return "NY SESSION - Maximum Liquidty"
    return "ASIAN SESSION - Slow Move"
