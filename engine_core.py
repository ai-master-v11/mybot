import pandas as pd
import numpy as np

def process_market_flow(data):
    # মার্কেট ফ্লো এবং ক্যান্ডেল রিদম চেক করার লজিক
    data['HL_Avg'] = (data['High'] + data['Low']) / 2
    flow_status = "STABLE"
    if data['Close'].iloc[-1] > data['HL_Avg'].iloc[-1]:
        flow_status = "BULLISH_FLOW"
    else:
        flow_status = "BEARISH_FLOW"
    return flow_status
