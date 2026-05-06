from datetime import datetime, timedelta

def get_next_candle_time():
    # পরবর্তী ক্যান্ডেলের সঠিক সময় বের করা
    now = datetime.now()
    next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    return next_minute.strftime("%H:%M:%S")
