import numpy as np

def forecast_next_decade(current_price):
    # আগামী ১০ বছরের প্রেডিকশন লজিক
    growth_factor = 1.05 # ৫% বাৎসরিক গ্রোথ ধরে
    forecast_2035 = current_price * (growth_factor ** 10)
    return round(forecast_2035, 4)
