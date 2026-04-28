def check_wick_rejection(candle_data):
    # candle_data = {'open': o, 'high': h, 'low': l, 'close': c, 'type': 'S/R_Level'}
    
    body_size = abs(candle_data['close'] - candle_data['open'])
    upper_wick = candle_data['high'] - max(candle_data['open'], candle_data['close'])
    lower_wick = min(candle_data['open'], candle_data['close']) - candle_data['low']

    # Resistance-এ লম্বা উপরের উইক (Sell Signal)
    if candle_data['type'] == 'Resistance' and upper_wick > (body_size * 2):
        return "SELL - Strong Resistance Rejection Detected!"

    # Support-এ লম্বা নিচের উইক (Buy Signal)
    elif candle_data['type'] == 'Support' and lower_wick > (body_size * 2):
        return "BUY - Strong Support Rejection Detected!"

    return "WAIT - No Strong Rejection"
def check_trend_continuation(candles):
    # candles = ৫টি ক্যান্ডেলের লিস্ট [c1, c2, c3, c4, c5]
    # c1 = বড় ক্যান্ডেল, c2-c4 = ছোট রিট্রেসমেন্ট, c5 = ব্রেকআউট ক্যান্ডেল

    # Rising Three Methods (UP Trend)
    if (candles[0].is_green and candles[0].body > candles[1].body * 2 and
        all(not c.is_green for c in candles[1:4]) and
        candles[4].is_green and candles[4].close > candles[0].high):
        return "STRONG BUY - Trend Continuation (Rising Three Methods)"

    # Falling Three Methods (DOWN Trend)
    elif (candles[0].is_red and candles[0].body > candles[1].body * 2 and
          all(c.is_green for c in candles[1:4]) and
          candles[4].is_red and candles[4].close < candles[0].low):
        return "STRONG SELL - Trend Continuation (Falling Three Methods)"

    return "HOLD - Trend and Correction logic not matching"
def check_belt_hold_logic(open, low, high, close, current_trend):
    # candle_data = ওপেন, হাই, লো, ক্লোজ এবং বর্তমান ট্রেন্ড
    
    body_size = abs(close - open)
    upper_wick = high - max(open, close)
    lower_wick = min(open, close) - low

    # Bullish Belt Hold: একদম লো-প্রাইসে ওপেন (উইক নেই), বডি অনেক বড়
    if current_trend == "Downtrend" and lower_wick == 0 and close > open:
        if body_size > (upper_wick * 3): # বডি উইকের তুলনায় অনেক বড় হতে হবে
            return "ULTRA BUY - Bullish Belt Hold! বায়াররা মার্কেট কবজা করেছে।"

    # Bearish Belt Hold: একদম হাই-প্রাইসে ওপেন (উপরে উইক নেই), বড় লাল বডি
    elif current_trend == "Uptrend" and upper_wick == 0 and close < open:
        if body_size > (lower_wick * 3):
            return "ULTRA SELL - Bearish Belt Hold! সেলাররা মার্কেট কবজা করেছে।"

    return "NEUTRAL - No Aggressive Belt Hold Detected"
def check_marubozu_power(open, high, low, close):
    # Marubozu মানে হলো এমন একটি ক্যান্ডেল যার কোনো উইক বা লেজ নেই
    # এটি মার্কেটে বায়ার বা সেলারদের চরম জেদ প্রকাশ করে।

    total_length = high - low
    body_size = abs(close - open)
    
    # যদি বডি ক্যান্ডেলের মোট দৈর্ঘ্যের ৯৫% এর বেশি হয় (অর্থাৎ উইক নেই বললেই চলে)
    if body_size >= (total_length * 0.95):
        if close > open:
            return "STRONG BUY - Bullish Marubozu! কোনো রিজেকশন নেই, বায়াররা পাগল হয়ে কিনছে।"
        else:
            return "STRONG SELL - Bearish Marubozu! কোনো সাপোর্ট নেই, সেলাররা মার্কেট ক্র্যাশ করাচ্ছে।"

    return "WAIT - Normal Candle (Indecision present)"
def check_star_reversal(candles):
    # candles = ৩টি ক্যান্ডেলের লিস্ট [c1, c2, c3]
    
    # Morning Star (Bullish Reversal - ডাউন্টেন্ডের শেষে)
    if (candles[0].is_red and candles[0].body > average_body_size and
        candles[1].body < candles[0].body * 0.3 and # মাঝখানের ক্যান্ডেলটি ছোট (Doji/Star)
        candles[2].is_green and candles[2].close > (candles[0].open + candles[0].close) / 2):
        return "MASTER BUY - Morning Star! অন্ধকারের পর নতুন সূর্য উঠছে।"

    # Evening Star (Bearish Reversal - আপট্রেন্ডের শেষে)
    elif (candles[1].is_green and candles[0].body > average_body_size and
          candles[1].body < candles[0].body * 0.3 and
          candles[2].is_red and candles[2].close < (candles[0].open + candles[0].close) / 2):
        return "MASTER SELL - Evening Star! ট্রেন্ড শেষ, এবার পতনের পালা।"

    return "SCANNING - No Star Pattern Found"
def check_indecision_logic(open, high, low, close):
    # Spinning Top বা Doji মানে হলো বায়ার এবং সেলার কেউ জিততে পারছে না
    
    body_size = abs(close - open)
    total_range = high - low
    upper_wick = high - max(open, close)
    lower_wick = min(open, close) - low

    # Doji Logic: যখন ওপেন আর ক্লোজ প্রায় সমান (বডি নেই বললেই চলে)
    if body_size <= (total_range * 0.1):
        return "ALERT - Doji Detected! মার্কেট এখন কনফিউজড, ব্রেকআউটের অপেক্ষা করো।"

    # Spinning Top Logic: ছোট বডি কিন্তু দুই দিকেই সমান লম্বা উইক
    elif body_size <= (total_range * 0.3) and abs(upper_wick - lower_wick) < (total_range * 0.1):
        return "ALERT - Spinning Top! ট্রেন্ডের শক্তি শেষ হয়ে আসছে, রিভার্সাল হতে পারে।"

    return "NORMAL - Momentum is still clear"
def check_engulfing_logic(prev_candle, curr_candle):
    # prev_candle = আগের ক্যান্ডেল, curr_candle = বর্তমান ক্যান্ডেল
    
    # Bullish Engulfing: আগের লাল ক্যান্ডেলকে সবুজ ক্যান্ডেল পুরো গিলে ফেলেছে
    if (prev_candle.is_red and curr_candle.is_green and 
        curr_candle.open <= prev_candle.close and 
        curr_candle.close > prev_candle.open):
        return "CONFIRMED BUY - Bullish Engulfing! বায়াররা সেলারদের পুরোপুরি গিলে ফেলেছে।"

    # Bearish Engulfing: আগের সবুজ ক্যান্ডেলকে লাল ক্যান্ডেল পুরো গিলে ফেলেছে
    elif (prev_candle.is_green and curr_candle.is_red and 
          curr_candle.open >= prev_candle.close and 
          curr_candle.close < prev_candle.open):
        return "CONFIRMED SELL - Bearish Engulfing! সেলাররা এখন মার্কেটের রাজা।"

    return "SCANNING - No Engulfing Pattern"
def check_tweezer_logic(candle1, candle2):
    # candle1 = আগের ক্যান্ডেল, candle2 = বর্তমান ক্যান্ডেল
    
    # Tweezer Bottom: দুইটা ক্যান্ডেলের লো (Low) প্রায় সমান (সাপোর্টে বায়ারদের দেওয়াল)
    if abs(candle1.low - candle2.low) < 0.00005: # প্রাইস গ্যাপ খুব সামান্য হলে
        if candle1.is_red and candle2.is_green:
            return "MASTER BUY - Tweezer Bottom! সাপোর্ট লেভেলে বায়ারদের শক্ত দেওয়াল।"

    # Tweezer Top: দুইটা ক্যান্ডেলের হাই (High) প্রায় সমান (রেজিস্ট্যান্সে সেলারদের দেওয়াল)
    elif abs(candle1.high - candle2.high) < 0.00005:
        if candle1.is_green and candle2.is_red:
            return "MASTER SELL - Tweezer Top! রেজিস্ট্যান্স লেভেলে সেলাররা ঢুকতে দিচ্ছে না।"

    return "NEUTRAL - No Tweezer Formation"
def check_harami_logic(mother_candle, baby_candle):
    # mother_candle = আগের বড় ক্যান্ডেল, baby_candle = বর্তমান ছোট ক্যান্ডেল
    
    # Bullish Harami (ডাউনট্রেন্ডের শেষে)
    if (mother_candle.is_red and baby_candle.is_green and 
        baby_candle.high < mother_candle.open and 
        baby_candle.low > mother_candle.close):
        return "CONFIRMED BUY - Bullish Harami! সেলারদের শক্তি শেষ, বায়াররা জন্ম নিচ্ছে।"

    # Bearish Harami (আপট্রেন্ডের শেষে)
    elif (mother_candle.is_green and baby_candle.is_red and 
          baby_candle.high < mother_candle.close and 
          baby_candle.low > mother_candle.open):
        return "CONFIRMED SELL - Bearish Harami! বায়াররা ক্লান্ত, সেলাররা মার্কেট ধরছে।"

    return "SCANNING - No Harami Pattern"
def check_50_percent_reversal(prev_candle, curr_candle):
    # prev_candle = আগের ক্যান্ডেল, curr_candle = বর্তমান ক্যান্ডেল
    prev_mid_point = (prev_candle.open + prev_candle.close) / 2
    
    # Piercing Line (Bullish - ডাউন্টেন্ডের শেষে)
    if (prev_candle.is_red and curr_candle.is_green and 
        curr_candle.open < prev_candle.low and # গ্যাপ ডাউন ওপেন
        curr_candle.close > prev_mid_point and # আগের লাল ক্যান্ডেলের ৫০% এর উপরে ক্লোজ
        curr_candle.close < prev_candle.open):
        return "STRONG BUY - Piercing Line! বায়াররা ৫০% এর বেশি রিকভারি করেছে।"

    # Dark Cloud Cover (Bearish - আপট্রেন্ডের শেষে)
    elif (prev_candle.is_green and curr_candle.is_red and 
          curr_candle.open > prev_candle.high and # গ্যাপ আপ ওপেন
          curr_candle.close < prev_mid_point and # আগের সবুজ ক্যান্ডেলের ৫০% এর নিচে ক্লোজ
          curr_candle.close > prev_candle.open):
        return "STRONG SELL - Dark Cloud Cover! সেলাররা মার্কেটে আধিপত্য ফিরে পেয়েছে।"

    return "NEUTRAL - Wait for 50% confirmation"
def check_abandoned_baby(c1, c2, c3):
    # c1 = বড় ক্যান্ডেল, c2 = দোজি/স্টার ক্যান্ডেল (মাঝখানের বাচ্চা), c3 = রিভার্সাল ক্যান্ডেল
    
    # Bullish Abandoned Baby (Buy Signal)
    if (c1.is_red and c2.body_size < (c1.body_size * 0.1) and 
        c2.high < c1.low and c2.high < c3.low and # c2 ক্যান্ডেলটি পুরোপুরি গ্যাপে ঝুলে আছে
        c3.is_green and c3.close > (c1.open + c1.close)/2):
        return "JACKPOT BUY - Abandoned Baby! মার্কেট এখান থেকে রকেটের মতো উপরে যাবে।"

    # Bearish Abandoned Baby (Sell Signal)
    elif (c1.is_green and c2.body_size < (c1.body_size * 0.1) and 
          c2.low > c1.high and c2.low > c3.high and 
          c3.is_red and c3.close < (c1.open + c1.close)/2):
        return "JACKPOT SELL - Abandoned Baby! মার্কেট নিচে নামার জন্য তৈরি।"

    return "SCANNING - No Baby Pattern"
def check_fakeout_trap(prev_candle, curr_candle, level_price, level_type):
    # level_type = "Support" অথবা "Resistance"
    
    # Bearish Fakeout (রেজিস্ট্যান্সের উপরে গিয়ে আবার নিচে আসা)
    if level_type == "Resistance":
        if prev_candle.high > level_price and prev_candle.close < level_price:
            if curr_candle.is_red and curr_candle.close < prev_candle.low:
                return "TRAP DETECTED - Sell Now! এটা ফেক ব্রেকআউট ছিল, বায়াররা ফেঁসে গেছে।"

    # Bullish Fakeout (সাপোর্টের নিচে গিয়ে আবার উপরে আসা)
    elif level_type == "Support":
        if prev_candle.low < level_price and prev_candle.close > level_price:
            if curr_candle.is_green and curr_candle.close > prev_candle.high:
                return "TRAP DETECTED - Buy Now! সেলারদের স্টপ লস খেয়ে মার্কেট উপরে যাচ্ছে।"

    return "NORMAL - Price action is stable"
def check_shooting_star(candle, trend):
    # trend = বর্তমান মার্কেট কি আপট্রেন্ডে আছে?
    
    body_size = abs(candle.close - candle.open)
    upper_wick = candle.high - max(candle.open, candle.close)
    lower_wick = min(candle.open, candle.close) - candle.low

    # আপট্রেন্ডের একদম মাথায় যদি লম্বা উপরের উইক থাকে
    if trend == "Uptrend" and upper_wick > (body_size * 3):
        if lower_wick < (body_size * 0.5): # নিচে উইক একদম ছোট বা নেই
            return "DANGER SELL - Shooting Star! প্রাইস রিজেকশন হয়েছে, মার্কেট নিচে নামবে।"

    return "SCANNING - No Shooting Star"
def check_hammer_logic(candle, trend):
    # candle = বর্তমান ক্যান্ডেল ডেটা
    # trend = বর্তমান মার্কেট কি ডাউন্টেন্ডে আছে?
    
    body_size = abs(candle.close - candle.open)
    upper_wick = candle.high - max(candle.open, candle.close)
    lower_wick = min(candle.open, candle.close) - candle.low

    # ডাউন্টেন্ডের শেষে যদি লম্বা নিচের উইক থাকে (হাতুড়ির মতো দেখতে)
    if trend == "Downtrend" and lower_wick > (body_size * 2.5):
        if upper_wick < (body_size * 0.5): # উপরে উইক নেই বললেই চলে
            return "MASTER BUY - Hammer Detected! সেলাররা শেষ, বায়াররা মার্কেট টেনে তুলছে।"

    return "SCANNING - No Hammer Pattern Found"
def check_inverted_pullback(candles, current_trend):
    # candles = ৫-৬টি ক্যান্ডেলের একটি লিস্ট
    
    first_big_drop = candles[0].is_red and candles[0].body > average_size
    small_green_pullback = all(c.is_green and c.body < candles[0].body * 0.4 for c in candles[1:4])
    breakout_red = candles[4].is_red and candles[4].close < candles[0].low

    if current_trend == "Downtrend" and first_big_drop and small_green_pullback and breakout_red:
        return "STRONG SELL - Inverted Pullback! বায়াররা চেষ্টা করেছিল কিন্তু সেলাররা আবার মার্কেট দখল করেছে।"

    return "WAITING - No clear pullback pattern"
def check_gap_fill_logic(prev_close, current_open, current_close, current_trend):
    # গ্যাপ ডাউনের ক্ষেত্রে (Gap Down)
    if current_trend == "Uptrend" and current_open < prev_close:
        # যদি বর্তমান ক্যান্ডেলটি সবুজ হয় এবং গ্যাপ পূরণ করার চেষ্টা করে
        if current_close >= prev_close:
            return "BUY - Gap Filled! মার্কেট এখন তার আগের আপট্রেন্ড কন্টিনিউ করবে।"

    # গ্যাপ আপের ক্ষেত্রে (Gap Up)
    elif current_trend == "Downtrend" and current_open > prev_close:
        # যদি বর্তমান ক্যান্ডেলটি লাল হয় এবং গ্যাপের নিচে ক্লোজ দেয়
        if current_close <= prev_close:
            return "SELL - Gap Filled! সেলাররা গ্যাপ ভরাট করে আবার মার্কেট নিচে নামাচ্ছে।"

    return "WAIT - Gap not filled or trend not confirmed"
def check_three_soldiers_crows(candles):
    # candles = শেষ ৩টি ক্যান্ডেলের লিস্ট [c1, c2, c3]

    # Three White Soldiers (শক্তিশালী আপট্রেন্ড শুরু)
    if (all(c.is_green for c in candles) and 
        candles[1].close > candles[0].close and candles[2].close > candles[1].close and
        all(c.body > average_body_size for c in candles)):
        return "STRONG BUY - Three White Soldiers! বায়াররা পুরো কন্ট্রোলে আছে।"

    # Three Black Crows (শক্তিশালী ডাউন্টেন্ড শুরু)
    elif (all(c.is_red for c in candles) and 
          candles[1].close < candles[0].close and candles[2].close < candles[1].close and
          all(c.body > average_body_size for c in candles)):
        return "STRONG SELL - Three Black Crows! সেলাররা মার্কেট দখল করেছে।"

    return "WAITING - Trend not strong enough"
def check_retest_confirmation(level_price, candles, level_type):
    # level_price = সাপোর্ট বা রেজিস্ট্যান্স লাইন
    # candles = শেষ ৩টি ক্যান্ডেল [c1, c2, c3]
    
    # Resistance Retest (Buy)
    if level_type == "Resistance":
        # c1 ব্রেক করেছে, c2 নিচে নেমে লেভেলে টাচ করেছে (রিটেস্ট), c3 আবার উপরে গেছে
        if candles[0].close > level_price and candles[1].low <= level_price and candles[2].is_green:
            return "MASTER BUY - Retest Successful! রেজিস্ট্যান্স এখন সাপোর্ট হয়ে গেছে।"

    # Support Retest (Sell)
    elif level_type == "Support":
        # c1 নিচে ব্রেক করেছে, c2 উপরে উঠে লেভেলে টাচ করেছে, c3 আবার নিচে গেছে
        if candles[0].close < level_price and candles[1].high >= level_price and candles[2].is_red:
            return "MASTER SELL - Retest Successful! সাপোর্ট এখন রেজিস্ট্যান্স হয়ে গেছে।"

    return "WAITING - Looking for a clean retest"
def check_rounding_pattern(candles, pattern_type):
    # candles = একটি বড় ক্যারেক্টারিস্টিক পিরিয়ডের ক্যান্ডেল লিস্ট
    # pattern_type = "Bottom" অথবা "Top"

    mid_index = len(candles) // 2
    
    # Rounding Bottom (Buy): প্রাইস ধীরে ধীরে কমে আবার ধীরে ধীরে বাড়তে শুরু করে
    if pattern_type == "Bottom":
        is_curving = all(candles[i].low >= candles[mid_index].low for i in range(len(candles)))
        if is_curving and candles[-1].close > max(candles[0].open, candles[0].close):
            return "LONG-TERM BUY - Rounding Bottom! স্মার্ট মানি অনেক সময় ধরে কিনছে।"

    # Rounding Top (Sell): প্রাইস ধীরে ধীরে উপরে উঠে আবার গোল হয়ে নিচে নামতে থাকে
    elif pattern_type == "Top":
        is_curving = all(candles[i].high <= candles[mid_index].high for i in range(len(candles)))
        if is_curving and candles[-1].close < min(candles[0].open, candles[0].close):
            return "LONG-TERM SELL - Rounding Top! বড় প্লেয়াররা ধীরে ধীরে হাত ধুয়ে ফেলছে।"

    return "SCANNING - Pattern still forming"
def check_wedge_squeeze(highs, lows, trend):
    # highs = ক্যান্ডেলগুলোর হাই পয়েন্টের লিস্ট, lows = লো পয়েন্টের লিস্ট
    
    # Rising Wedge (Bearish Reversal - উপরে উঠতে উঠতে সরু হওয়া)
    if trend == "Uptrend":
        # হাইগুলো আগের চেয়ে উপরে যাচ্ছে কিন্তু খুব ধীরগতিতে (Higher Highs)
        # লোগুলো অনেক দ্রুত উপরে উঠছে (Higher Lows) - অর্থাৎ রেঞ্জ সরু হচ্ছে
        if highs[-1] > highs[0] and (lows[-1] - lows[-2]) > (highs[-1] - highs[-2]):
            return "WARNING SELL - Rising Wedge! বায়াররা ক্লান্ত, মার্কেট ধপাস করে পড়বে।"

    # Falling Wedge (Bullish Reversal - নিচে নামতে নামতে সরু হওয়া)
    elif trend == "Downtrend":
        # লোগুলো নিচে নামছে ধীরগতিতে, হাইগুলো দ্রুত নিচে নামছে (রেঞ্জ সরু হচ্ছে)
        if lows[-1] < lows[0] and (highs[-2] - highs[-1]) > (lows[-2] - lows[-1]):
            return "WARNING BUY - Falling Wedge! সেলাররা শেষ, মার্কেট রকেটের মতো উঠবে।"

    return "SCANNING - Market range is normal"
def check_kicking_logic(prev_candle, curr_candle):
    # Bullish Kicking: আগের লাল মারুবোজুর পর গ্যাপ-আপ দিয়ে সবুজ মারুবোজু
    if (prev_candle.is_red and prev_candle.lower_wick == 0 and prev_candle.upper_wick == 0 and
        curr_candle.is_green and curr_candle.open > prev_candle.open and 
        curr_candle.lower_wick == 0 and curr_candle.upper_wick == 0):
        return "ULTRA BUY - Bullish Kicking! সেলারদের পাত্তাই দেয়নি বায়াররা।"

    # Bearish Kicking: আগের সবুজ মারুবোজুর পর গ্যাপ-ডাউন দিয়ে লাল মারুবোজু
    elif (prev_candle.is_green and prev_candle.lower_wick == 0 and prev_candle.upper_wick == 0 and
          curr_candle.is_red and curr_candle.open < prev_candle.open and 
          curr_candle.lower_wick == 0 and curr_candle.upper_wick == 0):
        return "ULTRA SELL - Bearish Kicking! বায়ারদের পিষে ফেলেছে সেলাররা।"

    return "SCANNING - No Kicking Pattern detected"
def check_inside_bar_breakout(mother_candle, inside_candle, trigger_candle):
    # mother_candle = আগের বড় ক্যান্ডেল, inside_candle = তার পেটের ভেতরের ক্যান্ডেল
    
    # ইনসাইড বার কনফার্মেশন (মা ক্যান্ডেলের হাই-লো এর ভেতরে বাচ্চা ক্যান্ডেল)
    is_inside = (inside_candle.high < mother_candle.high and 
                 inside_candle.low > mother_candle.low)
    
    if is_inside:
        # Bullish Breakout: যদি ৩ নম্বর ক্যান্ডেল মা ক্যান্ডেলের হাই ব্রেক করে
        if trigger_candle.close > mother_candle.high:
            return "ROCKET BUY - Inside Bar Breakout! স্প্রিং লোড হয়ে উপরে ছুটছে।"
            
        # Bearish Breakout: যদি ৩ নম্বর ক্যান্ডেল মা ক্যান্ডেলের লো ব্রেক করে
        elif trigger_candle.close < mother_candle.low:
            return "CRASH SELL - Inside Bar Breakout! নিচের দিকে বড় ফল (Fall) আসছে।"

    return "COILING - Market is still inside, wait for breakout"
def check_triple_reversal(peaks, level_type):
    # peaks = তিনটি পরপর হাই বা লো পয়েন্টের লিস্ট [p1, p2, p3]
    
    # Triple Top (রেজিস্ট্যান্সে তিনবার ধাক্কা খেয়ে নিচে নামা)
    if level_type == "Resistance":
        if abs(peaks[0] - peaks[1]) < 0.0001 and abs(peaks[1] - peaks[2]) < 0.0001:
            return "MAJOR SELL - Triple Top! সেলাররা তিনবার রেজিস্ট্যান্স রক্ষা করেছে।"

    # Triple Bottom (সাপোর্টে তিনবার ধাক্কা খেয়ে উপরে ওঠা)
    elif level_type == "Support":
        if abs(peaks[0] - peaks[1]) < 0.0001 and abs(peaks[1] - peaks[2]) < 0.0001:
            return "MAJOR BUY - Triple Bottom! বায়াররা শক্ত অবস্থানে, ট্রেন্ড ঘুরছে।"

    return "SCANNING - Pattern not complete yet"
def check_volume_breakout(candle, avg_volume, resistance_level):
    # candle = বর্তমান ক্যান্ডেল, avg_volume = গত ২০টি ক্যান্ডেলের গড় ভলিউম
    
    # Resistance Breakout with Volume
    if candle.close > resistance_level:
        if candle.volume > (avg_volume * 1.5): # ভলিউম গড়ের দেড় গুণের বেশি
            return "CONFIRMED BUY - Real Breakout! বড় প্লেয়াররা ভলিউম নিয়ে ঢুকেছে।"
        else:
            return "AVOID BUY - Weak Breakout! ভলিউম নেই, এটা একটা ফেক ট্র্যাপ হতে পারে।"

    return "SCANNING - Price below resistance"
def check_three_drive_logic(drives):
    # drives = ৩টি উচ্চতা বা লো এর লিস্ট [Drive1, Drive2, Drive3]
    
    # Bearish Three-Drive (সেলারদের জন্য)
    if (drives[2] > drives[1] > drives[0] and 
        (drives[2] - drives[1]) < (drives[1] - drives[0])):
        # ড্রাইভগুলোর দূরত্ব কমে আসছে মানে শক্তি হারাচ্ছে
        return "CRITICAL SELL - Three-Drive Pattern! বায়াররা হাঁপিয়ে গেছে, বড় ড্রপ আসছে।"

    # Bullish Three-Drive (বায়ারদের জন্য)
    elif (drives[2] < drives[1] < drives[0] and 
          (drives[1] - drives[2]) < (drives[0] - drives[1])):
        return "CRITICAL BUY - Three-Drive Pattern! সেলাররা শেষ, মার্কেট রকেটের মতো উঠবে।"

    return "SCANNING - Market moving normally"
def check_pin_bar_logic(candle):
    body_size = abs(candle.close - candle.open)
    total_length = candle.high - candle.low
    upper_shadow = candle.high - max(candle.open, candle.close)
    lower_shadow = min(candle.open, candle.close) - candle.low

    # Bullish Pin Bar: নিচের দিকে লম্বা লেজ (প্রাইস নিচে থাকতে পারেনি)
    if lower_shadow > (body_size * 3) and upper_shadow < body_size:
        return "MASTER BUY - Bullish Pin Bar! সেলাররা ধাক্কা দিয়েছিল কিন্তু বায়াররা দখল নিয়েছে।"

    # Bearish Pin Bar: উপরের দিকে লম্বা লেজ (প্রাইস উপরে থাকতে পারেনি)
    elif upper_shadow > (body_size * 3) and lower_shadow < body_size:
        return "MASTER SELL - Bearish Pin Bar! বায়াররা ব্যর্থ, সেলাররা এখন শক্তিশালী।"

    return "NEUTRAL - No Pin Bar detected"
def check_tweezers_logic(prev_candle, curr_candle):
    # Tweezers Bottom (Buy): দুটি ক্যান্ডেলের লো প্রায় একই জায়গায়
    if (abs(prev_candle.low - curr_candle.low) < 0.00005 and 
        prev_candle.is_red and curr_candle.is_green):
        return "STRONG BUY - Tweezers Bottom! সাপোর্ট অনেক শক্তিশালী, মার্কেট এখান থেকে ফিরবে।"

    # Tweezers Top (Sell): দুটি ক্যান্ডেলের হাই প্রায় একই জায়গায়
    elif (abs(prev_candle.high - curr_candle.high) < 0.00005 and 
          prev_candle.is_green and curr_candle.is_red):
        return "STRONG SELL - Tweezers Top! রেজিস্ট্যান্স ব্রেক করতে পারেনি, এবার পতন নিশ্চিত।"

    return "SCANNING - No Tweezers pattern"
def check_star_reversal(c1, c2, c3):
    # c1 = বড় ক্যান্ডেল, c2 = ছোট ক্যান্ডেল (স্টার), c3 = রিভার্সাল ক্যান্ডেল
    
    # Morning Star (Buy): ডাউন্টেন্ডের পর তৈরি হয়
    if c1.is_red and abs(c2.open - c2.close) < (c1.body * 0.3):
        if c3.is_green and c3.close > (c1.open + c1.close) / 2:
            return "ULTRA BUY - Morning Star! অন্ধকার শেষ, নতুন ট্রেন্ড শুরু।"

    # Evening Star (Sell): আপট্রেন্ডের পর তৈরি হয়
    elif c1.is_green and abs(c2.open - c2.close) < (c1.body * 0.3):
        if c3.is_red and c3.close < (c1.open + c1.close) / 2:
            return "ULTRA SELL - Evening Star! আলো নিভে আসছে, এবার মার্কেট নামবে।"

    return "SCANNING - Stars not aligned yet"
def check_fakeout_squeeze(prev_candles, breakout_candle, confirmation_candle, level):
    # ব্রেকআউট ক্যান্ডেল যদি লেভেলের উপরে ক্লোজ দেয়
    if breakout_candle.close > level and all(c.close < level for c in prev_candles):
        # কিন্তু পরের ক্যান্ডেলটিই যদি আবার লেভেলের নিচে চলে আসে (ফেক আউট)
        if confirmation_candle.close < level and confirmation_candle.is_red:
            return "DANGER - Fakeout Squeeze! বায়াররা ফেঁসে গেছে, এবার বড় সেল আসবে।"
            
    return "STABLE - No fakeout detected"
def check_three_methods(candles):
    # candles = ৫টি ক্যান্ডেলের লিস্ট [c1, c2, c3, c4, c5]
    
    # Rising Three Methods (Bullish Continuation)
    first_big_green = candles[0].is_green and candles[0].body > average_body
    small_red_rest = all(c.is_red and c.high < candles[0].high for c in candles[1:4])
    final_breakout = candles[4].is_green and candles[4].close > candles[0].high

    if first_big_green and small_red_rest and final_breakout:
        return "TREND CONTINUE - Rising Three Methods! মার্কেট একটু জিরিয়ে নিয়ে আবার উপরে ছুটছে।"

    # Falling Three Methods (Bearish Continuation)
    first_big_red = candles[0].is_red and candles[0].body > average_body
    small_green_rest = all(c.is_green and c.low > candles[0].low for c in candles[1:4])
    final_breakdown = candles[4].is_red and candles[4].close < candles[0].low

    if first_big_red and small_green_rest and final_breakdown:
        return "TREND CONTINUE - Falling Three Methods! সেলাররা একটু বিশ্রাম নিয়ে আবার নিচে নামাচ্ছে।"

    return "SCANNING - Consolidation in progress"
def check_exhaustion_logic(prev_candles, current_candle, trend):
    avg_body_size = sum(abs(c.close - c.open) for c in prev_candles) / len(prev_candles)
    
    # বর্তমান ক্যান্ডেল যদি গড়ের চেয়ে ৩ গুণের বেশি বড় হয়
    is_giant_candle = abs(current_candle.close - current_candle.open) > (avg_body_size * 3)

    # আপট্রেন্ডের শেষে বিশাল সবুজ ক্যান্ডেল (Buying Exhaustion)
    if trend == "Uptrend" and current_candle.is_green and is_giant_candle:
        return "BEWARE - Buying Exhaustion! বায়াররা তাদের শেষ শক্তি খরচ করে ফেলেছে। এবার পতন নিশ্চিত।"

    # ডাউন্টেন্ডের শেষে বিশাল লাল ক্যান্ডেল (Selling Exhaustion)
    elif trend == "Downtrend" and current_candle.is_red and is_giant_candle:
        return "BEWARE - Selling Exhaustion! সেলারদের সব শক্তি শেষ। এখান থেকে মার্কেট ঘুরে দাঁড়াবে।"

    return "SCANNING - Market moving with normal volume"
def check_engulfing_logic(prev_candle, curr_candle):
    # Bullish Engulfing: আগের ছোট লাল ক্যান্ডেলকে পরের বড় সবুজ ক্যান্ডেল গ্রাস করেছে
    if (prev_candle.is_red and curr_candle.is_green and 
        curr_candle.open < prev_candle.close and curr_candle.close > prev_candle.open):
        return "SUPER BUY - Bullish Engulfing! বায়াররা সেলারদের পুরো গিলে ফেলেছে।"

    # Bearish Engulfing: আগের ছোট সবুজ ক্যান্ডেলকে পরের বড় লাল ক্যান্ডেল গ্রাস করেছে
    elif (prev_candle.is_green and curr_candle.is_red and 
          curr_candle.open > prev_candle.close and curr_candle.close < prev_candle.open):
        return "SUPER SELL - Bearish Engulfing! সেলাররা বায়ারদের হটিয়ে মার্কেট দখল করেছে।"

    return "SCANNING - Waiting for power shift"
def check_bollinger_squeeze(upper_band, lower_band, current_price):
    band_width = upper_band - lower_band
    
    # যদি ব্যান্ড দুটির দূরত্ব গড়ের চেয়ে অনেক কমে যায় (Squeeze)
    if band_width < average_historical_width * 0.5:
        # ব্রেকআউট চেনার উপায়
        if current_price > upper_band:
            return "VOLATILITY EXPLOSION BUY! স্প্রিং ছাড়া পেয়েছে, উপরে ছুটবে।"
        elif current_price < lower_band:
            return "VOLATILITY EXPLOSION SELL! নিচের দিকে বড় ধস নামছে।"
            
    return "MARKET SLEEPING - Narrow range, do not trade"
def check_shooting_star(candle):
    body_size = abs(candle.close - candle.open)
    upper_shadow = candle.high - max(candle.open, candle.close)
    lower_shadow = min(candle.open, candle.close) - candle.low
    
    # শুটিং স্টার কন্ডিশন: উপরের লেজ বডির তুলনায় অন্তত ৩ গুণ বড়
    if upper_shadow > (body_size * 3) and lower_shadow < (body_size * 0.5):
        return "CRITICAL SELL - Shooting Star! বায়াররা আকাশ ছুঁতে চেয়েছিল কিন্তু সেলাররা মাটিতে আছড়ে ফেলেছে।"

    return "SCANNING - Sky is clear"
def check_hammer_logic(candle):
    body_size = abs(candle.close - candle.open)
    lower_shadow = min(candle.open, candle.close) - candle.low
    upper_shadow = candle.high - max(candle.open, candle.close)
    
    # হ্যামার কন্ডিশন: নিচের লেজ বডির তুলনায় অন্তত ২-৩ গুণ বড় হতে হবে
    if lower_shadow > (body_size * 2) and upper_shadow < (body_size * 0.5):
        return "ROCKET BUY - Hammer Pattern! সেলাররা গর্ত খুঁড়েছিল কিন্তু বায়াররা সিঁড়ি বানিয়ে ফেলেছে।"

    return "SCANNING - Market still looking for a bottom"
def check_gap_fill(prev_candle_close, curr_candle_open, current_price):
    # গ্যাপ ডাউনের ক্ষেত্রে (Gap Down)
    if curr_candle_open < (prev_candle_close - threshold):
        # যদি প্রাইস আবার উপরে উঠতে শুরু করে ওই গ্যাপের দিকে
        if current_price > curr_candle_open:
            return "BUY TARGET - Gap Fill! মার্কেট তার পুরোনো ঋণ শোধ করতে উপরে উঠছে।"

    # গ্যাপ আপের ক্ষেত্রে (Gap Up)
    elif curr_candle_open > (prev_candle_close + threshold):
        # যদি প্রাইস নিচে নামতে শুরু করে গ্যাপের দিকে
        if current_price < curr_candle_open:
            return "SELL TARGET - Gap Fill! ওপরের গ্যাপ পূরণ করতে মার্কেট নিচে নামছে।"

    return "STABLE - No major gap to fill"def check_flag_pattern(pole_size, consolidation_range, current_breakout):
    # pole_size = আগের বড় মুভমেন্ট (খুঁটি)
    # consolidation_range = ছোট ছোট ক্যান্ডেলের রেঞ্জ (পতাকা)
    
    # বুলিশ ফ্ল্যাগ: উপরে ওঠার পর একটু জিরিয়ে আবার ব্রেকআউট
    if pole_size > average_move * 2:
        if consolidation_range < (pole_size * 0.3): # পতাকাটি খুঁটির তুলনায় ছোট
            if current_breakout > max_consolidation:
                return "TREND ROCKET BUY - Flag Breakout! বিরতি শেষ, এবার লক্ষ্য আরও উপরে।"

    return "WAITING - Flag is still forming or no pole detected"
def check_doji_logic(candle):
    body_size = abs(candle.close - candle.open)
    total_range = candle.high - candle.low
    
    # দোজি কন্ডিশন: বডি হবে মোট রেঞ্জের তুলনায় একদম নগণ্য (৫-১০%)
    if body_size < (total_range * 0.1):
        return "NEUTRAL - Doji Detected! মার্কেট এখন দোটানায়, ব্রেকআউটের জন্য অপেক্ষা করো।"

    # ড্রাগনফ্লাই দোজি (Bullish Reversal signal at support)
    if body_size < (total_range * 0.1) and (candle.high - max(candle.open, candle.close)) < (total_range * 0.1):
        return "POTENTIAL BUY - Dragonfly Doji! নিচে রিজেকশন, বায়াররা কন্ট্রোল নিচ্ছে।"
def check_harami_logic(mother_candle, baby_candle):
    # Bullish Harami: বড় লাল ক্যান্ডেলের পেটের ভেতর ছোট সবুজ ক্যান্ডেল
    if (mother_candle.is_red and baby_candle.is_green and 
        baby_candle.high < mother_candle.open and baby_candle.low > mother_candle.close):
        return "REVERSAL ALERT - Bullish Harami! পতন থামার সংকেত, বায়াররা উঁকি দিচ্ছে।"

    # Bearish Harami: বড় সবুজ ক্যান্ডেলের পেটের ভেতর ছোট লাল ক্যান্ডেল
    elif (mother_candle.is_green and baby_candle.is_red and 
          baby_candle.high < mother_candle.close and baby_candle.low > mother_candle.open):
        return "REVERSAL ALERT - Bearish Harami! উত্থান থামার সংকেত, সেলাররা ভেতরে ঢুকেছে।"

    return "SCANNING - Trend is still dominant"
def check_three_soldiers_crows(c1, c2, c3):
    # Three White Soldiers (বুলিশ কনফার্মেশন কিন্তু অতিরিক্ত বাড়লে সাবধান)
    if c1.is_green and c2.is_green and c3.is_green:
        if c3.close > c2.close > c1.close:
            return "TREND STRONG BUY - Three White Soldiers! বায়াররা পুরো কন্ট্রোলে।"

    # Three Black Crowes (বেয়ারিশ কনফার্মেশন কিন্তু অতিরিক্ত পড়লে সাবধান)
    elif c1.is_red and c2.is_red and c3.is_red:
        if c3.close < c2.close < c1.close:
            return "TREND STRONG SELL - Three Black Crows! সেলাররা মার্কেট দখল করেছে।"

    return "SCANNING - Market seeking direction"
def check_spinning_top(candle):
    body_size = abs(candle.close - candle.open)
    upper_shadow = candle.high - max(candle.open, candle.close)
    lower_shadow = min(candle.open, candle.close) - candle.low
    
    # স্পিনিং টপ কন্ডিশন: বডি ছোট কিন্তু দুই পাশের লেজ প্রায় সমান এবং লম্বা
    if body_size < (candle.high - candle.low) * 0.3:
        if abs(upper_shadow - lower_shadow) < (body_size * 0.5):
            return "WARNING - Spinning Top! বায়ার-সেলার কেউ হার মানছে না। যেদিকে ব্রেকআউট হবে, সেদিকেই ট্রেড নাও।"

    return "SCANNING - Market has a clear leader"
def check_piercing_line(prev_red, curr_green):
    # ১. প্রথম ক্যান্ডেলটি অবশ্যই বড় লাল হতে হবে
    # ২. দ্বিতীয় ক্যান্ডেলটি আগের চেয়ে নিচ থেকে শুরু হবে (Gap Down)
    # ৩. দ্বিতীয় ক্যান্ডেলের ক্লোজিং আগের লাল ক্যান্ডেলের অন্তত ৫০% উপরে হতে হবে
    
    red_midpoint = (prev_red.open + prev_red.close) / 2
    
    if (prev_red.is_red and curr_green.is_green and 
        curr_green.open < prev_red.low and 
        curr_green.close > red_midpoint and 
        curr_green.close < prev_red.open):
        return "CONFIRMED BUY - Piercing Line! বায়াররা সেলারদের অর্ধেক দুর্গ দখল করে নিয়েছে।"

    return "SCANNING - Looking for the pierce"
def check_dark_cloud_cover(prev_green, curr_red):
    # ১. প্রথম ক্যান্ডেলটি অবশ্যই বড় সবুজ হতে হবে
    # ২. দ্বিতীয় ক্যান্ডেলটি আগের চেয়ে উপর থেকে শুরু হবে (Gap Up)
    # ৩. দ্বিতীয় ক্যান্ডেলের ক্লোজিং আগের সবুজ ক্যান্ডেলের অন্তত ৫০% নিচে হতে হবে
    
    green_midpoint = (prev_green.open + prev_green.close) / 2
    
    if (prev_green.is_green and curr_red.is_red and 
        curr_red.open > prev_green.high and 
        curr_red.close < green_midpoint and 
        curr_red.close > prev_green.open):
        return "STRONG SELL - Dark Cloud Cover! বায়ারদের আকাশে মেঘ জমেছে, এবার ধস নামবে।"

    return "SCANNING - Sky is still clear"
def check_tweezer_rejection(c1, c2, level_type):
    # c1 এবং c2 এর উইক যদি প্রায় একই লেভেলে রিজেকশন পায়
    
    # Resistance এ Tweezer Top
    if level_type == "Resistance":
        if abs(c1.high - c2.high) < 0.00002 and c1.upper_wick > c1.body:
            return "SURE SELL - Tweezer Top Rejection! এই দেয়াল বায়াররা ভাঙতে পারবে না।"

    # Support এ Tweezer Bottom
    elif level_type == "Support":
        if abs(c1.low - c2.low) < 0.00002 and c1.lower_wick > c1.body:
            return "SURE BUY - Tweezer Bottom Rejection! নিচ থেকে বায়াররা কড়া পাহারা দিচ্ছে।"

    return "SCANNING - No twin rejection found"

def check_hanging_man(candle, trend):
    body_size = abs(candle.close - candle.open)
    lower_shadow = min(candle.open, candle.close) - candle.low
    upper_shadow = candle.high - max(candle.open, candle.close)
    
    # হ্যাংগিং ম্যান কন্ডিশন: আপট্রেন্ড থাকতে হবে এবং নিচের লেজ বডির ২ গুণের বেশি বড় হতে হবে
    if trend == "Uptrend" and lower_shadow > (body_size * 2) and upper_shadow < (body_size * 0.3):
        return "WARNING SELL - Hanging Man! বায়াররা ঝুলে আছে, যেকোনো সময় ধস নামতে পারে।"

    return "SCANNING - Trend looks stable"
def check_star_momentum(prev_big_candle, current_small_candle):
    # আগের ক্যান্ডেলটি অনেক বড় হতে হবে
    # বর্তমান ক্যান্ডেলটির বডি আগেরটির তুলনায় অন্তত ৭০% ছোট হতে হবে
    # দুটোর মাঝখানে ছোট একটি গ্যাপ থাকা ভালো
    
    if abs(prev_big_candle.open - prev_big_candle.close) > average_body * 2:
        if abs(current_small_candle.open - current_small_candle.close) < average_body * 0.5:
            return "CAUTION - Star Detected! দৌড় থামছে, এবার উল্টো দিকে ঘোরার পালা।"

    return "SCANNING - Momentum is still high"
def check_fakeout(candle, level):
    # Resistance ব্রেকআউটের চেষ্টা
    if candle.high > level:
        # কিন্তু ক্যান্ডেলটি যদি লেভেলের নিচে ক্লোজ দেয় এবং বড় উইক থাকে
        if candle.close < level and (candle.high - level) > (abs(candle.open - candle.close)):
            return "BEWARE - Fakeout Detected! বায়াররা ফেঁসে গেছে, এবার সেল করো।"

    # Support ব্রেকআউটের চেষ্টা
    elif candle.low < level:
        if candle.close > level and (level - candle.low) > (abs(candle.open - candle.close)):
            return "BEWARE - Fakeout Detected! সেলাররা ট্র্যাপে পড়েছে, এবার বাই করো।"

    return "SCANNING - Waiting for real breakout"
def check_morning_star(c1, c2, c3):
    # c1: বড় লাল ক্যান্ডেল (সেলাররা শক্তিশালী)
    # c2: ছোট বডির ক্যান্ডেল বা দোজি (বায়ার-সেলার সমান সমান)
    # c3: বড় সবুজ ক্যান্ডেল (বায়াররা ফিরে এসেছে)

    if c1.is_red and abs(c1.open - c1.close) > average_body:
        if abs(c2.open - c2.close) < (average_body * 0.3): # ছোট বডি
            if c3.is_green and c3.close > ((c1.open + c1.close) / 2):
                return "SUPER BUY - Morning Star! অন্ধকার শেষ, এবার মার্কেট উপরে দৌড়াবে।"

    return "SCANNING - Looking for the star in the dark"
def check_evening_star(c1, c2, c3):
    # c1: বড় সবুজ ক্যান্ডেল (বায়াররা পূর্ণ শক্তিতে)
    # c2: ছোট বডির ক্যান্ডেল বা স্টার (বায়ারদের ক্লান্তি)
    # c3: বড় লাল ক্যান্ডেল (সেলারদের প্রচণ্ড আক্রমণ)

    if c1.is_green and abs(c1.open - c1.close) > average_body:
        if abs(c2.open - c2.close) < (average_body * 0.3): # ছোট বডি
            if c3.is_red and c3.close < ((c1.open + c1.close) / 2):
                return "SUPER SELL - Evening Star! দিন শেষ, এবার রাত নামবে (মার্কেট পড়বে)।"

    return "SCANNING - Sky is still bright"
def check_golden_rejection(touch_points, current_price):
    # touch_points = লেভেলে কতবার টাচ করেছে তার সংখ্যা
    
    if touch_points == 3:
        if is_rejection_candle(current_candle): # যদি পিনবার বা হ্যামার তৈরি হয়
            return "GOLDEN ENTRY - 3rd Tap Logic! এটা মিস করা পাপ। বিশাল রিভার্সাল আসছে।"
    
    elif touch_points > 3:
        return "WARNING - Level getting weak. এবার ব্রেকআউট হতে পারে।"

    return "SCANNING - Counting touch points..."
def check_three_inside_logic(c1, c2, c3):
    # Three Inside Up (বুলিশ রিভার্সাল)
    if c1.is_red and is_harami(c1, c2): # প্রথম দুটি হারামি প্যাটার্ন
        if c3.is_green and c3.close > c1.open:
            return "ULTRA BUY - Three Inside Up! মার্কেট এখন পুরোপুরি বায়ারদের দখলে।"

    # Three Inside Down (বেয়ারিশ রিভার্সাল)
    elif c1.is_green and is_harami(c1, c2):
        if c3.is_red and c3.close < c1.open:
            return "ULTRA SELL - Three Inside Down! সেলাররা মার্কেটের নিয়ন্ত্রণ ছিনিয়ে নিয়েছে।"

    return "SCANNING - Waiting for 3rd candle confirmation"
def check_window_gap(prev_candle, current_candle):
    # Bullish Window (Gap Up)
    if current_candle.open > prev_candle.high:
        gap_level = prev_candle.high
        return f"GAP DETECTED - মার্কেট {gap_level} এ ফিরে আসতে পারে। গ্যাপ পূরণ হলে বাই এন্ট্রি নাও।"

    # Bearish Window (Gap Down)
    elif current_candle.open < prev_candle.low:
        gap_level = prev_candle.low
        return f"GAP DETECTED - মার্কেট {gap_level} এ রিটেস্ট করতে যাবে। গ্যাপ পূরণ হলে সেল করো।"

    return "SCANNING - No window/gap found"
def check_shooting_star(candle, trend):
    body_size = abs(candle.close - candle.open)
    upper_shadow = candle.high - max(candle.open, candle.close)
    lower_shadow = min(candle.open, candle.close) - candle.low
    
    # শুটিং স্টার কন্ডিশন: আপট্রেন্ডে থাকতে হবে, ওপরের লেজ বডির অন্তত ২ গুণের বেশি লম্বা হতে হবে।
    if trend == "Uptrend" and upper_shadow > (body_size * 2) and lower_shadow < (body_size * 0.3):
        return "CRITICAL SELL - Shooting Star! বায়াররা আকাশ থেকে মাটিতে আছড়ে পড়েছে।"

    return "SCANNING - Bulls are still pushing"def check_inside_bar(mother_bar, inside_bar):
    # ইনসাইড বার কন্ডিশন: মাদার বারের হাই এবং লো এর মাঝখানে ইনসাইড বারটি থাকবে
    if inside_bar.high < mother_bar.high and inside_bar.low > mother_bar.low:
        return "COILING - Inside Bar Detected! মার্কেট শক্তি জমা করছে। ব্রেকআউটের জন্য ওত পেতে থাকো।"

    # ব্রেকআউট লজিক
    if current_price > mother_bar.high:
        return "AGGRESSIVE BUY - Mother Bar Breakout! স্প্রিং খুলে গেছে, মার্কেট উপরে ছুটবে।"
    elif current_price < mother_bar.low:
        return "AGGRESSIVE SELL - Mother Bar Breakdown! নিচের দিকে বিস্ফোরণ।"

    return "WAITING - Price still inside mother bar range"
def check_whiplash_logic(reversal_candle, confirmation_candle, trend):
    # যদি একটি হ্যামার (বুলিশ রিভার্সাল) তৈরি হয় কিন্তু পরের ক্যান্ডেলটি তার নিচেই ক্লোজ দেয়
    if reversal_candle.type == "Hammer" and trend == "Downtrend":
        if confirmation_candle.close < reversal_candle.low:
            return "DANGER - False Reversal! বায়াররা ট্র্যাপে পড়েছে। সেলিং কন্টিনিউ করো।"

    # যদি একটি শুটিং স্টার তৈরি হয় কিন্তু পরের ক্যান্ডেলটি তার ওপরে ক্লোজ দেয়
    if reversal_candle.type == "Shooting_Star" and trend == "Uptrend":
        if confirmation_candle.close > reversal_candle.high:
            return "DANGER - False Reversal! সেলাররা ফেঁসে গেছে। বায়িং কন্টিনিউ করো।"
def check_triple_impact(peaks, current_price, level_type):
    # peaks = একই লেভেলে টাচ করা ক্যান্ডেলগুলোর সংখ্যা
    
    if len(peaks) == 3:
        if level_type == "Top":
            # তিনবার উপরে ধাক্কা খেয়ে ব্যর্থ হওয়া
            return "MASSIVE REVERSAL - Triple Top! আকাশ ছোঁয়া আর সম্ভব না, এবার নিচে নামার সময়।"
        
        elif level_type == "Bottom":
            # তিনবার নিচে ধাক্কা খেয়ে ফিরে আসা
            return "MASSIVE REVERSAL - Triple Bottom! পাথুরে দেয়াল, মার্কেট এখান থেকে রকেট হবে।"

    return "SCANNING - Counting the wall hits..."
def check_spinning_top(candle):
    body_size = abs(candle.close - candle.open)
    upper_shadow = candle.high - max(candle.open, candle.close)
    lower_shadow = min(candle.open, candle.close) - candle.low
    
    # স্পিনিং টপ কন্ডিশন: বডি হবে ছোট, আর দুই পাশের লেজ হবে প্রায় সমান ও বড়
    if body_size < (average_body * 0.5) and abs(upper_shadow - lower_shadow) < (body_size * 0.2):
        return "INDECISION - Spinning Top Detected! বায়ার-সেলার দুজনেই ক্লান্ত। রিভার্সাল আসতে পারে।"

    return "SCANNING - Market has a clear direction"
def check_army_formation(c1, c2, c3):
    # Three White Soldiers (বুলিশ ট্রেন্ডের শুরু)
    if (c1.is_green and c2.is_green and c3.is_green and
        c2.open > c1.open and c2.open < c1.close and
        c3.open > c2.open and c3.open < c2.close):
        return "TREND EXPLOSION - Three White Soldiers! বায়ারদের সেনাবাহিনী আক্রমণ শুরু করেছে।"

    # Three Black Crows (বেয়ারিশ ট্রেন্ডের শুরু)
    if (c1.is_red and c2.is_red and c3.is_red and
        c2.open < c1.open and c2.open > c1.close and
        c3.open < c2.open and c3.open > c2.close):
        return "TREND COLLAPSE - Three Black Crows! সেলারদের রাজত্ব শুরু, মার্কেট ধসে পড়বে।"

    return "SCANNING - Looking for army formation"
def check_advance_block(c1, c2, c3):
    # তিনটিই সবুজ ক্যান্ডেল হতে হবে
    if c1.is_green and c2.is_green and c3.is_green:
        # বডিগুলো ক্রমান্বয়ে ছোট হতে হবে
        if (c1.body > c2.body) and (c2.body > c3.body):
            # ওপরের উইকগুলো লম্বা হতে হবে (রিজেকশন)
            if c2.upper_wick > 0 and c3.upper_wick > c2.upper_wick:
                return "WARNING - Advance Block! বায়াররা হাঁপিয়ে গেছে। যেকোনো সময় মার্কেট ধপাস করে পড়বে।"

    return "SCANNING - Momentum seems healthy"
def check_flag_pattern(pole_candle, consolidation_candles, trend):
    # ১. প্রথমে একটি বড় ক্যান্ডেল থাকতে হবে (Strong Momentum)
    # ২. এরপর ৩-৫টি ছোট ক্যান্ডেল বিপরীত দিকে হালকা হেলে থাকবে (Consolidation)
    
    is_pole = abs(pole_candle.open - pole_candle.close) > (average_body * 2)
    is_consolidating = all(abs(c.open - c.close) < average_body for c in consolidation_candles)

    if is_pole and is_consolidating:
        if trend == "Uptrend":
            return "READY TO FLY - Bullish Flag! মার্কেট একটু জিরিয়ে নিয়ে আবার উপরে উড়াল দেবে।"
        elif trend == "Downtrend":
            return "READY TO DROP - Bearish Flag! নিচে পড়ার আগে এটা কেবল একটু বিরতি।"

    return "SCANNING - Looking for the pole and flag"
def check_two_rabbits_trap(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি বড় লাল (Bearish)
    # ২. দ্বিতীয় ক্যান্ডেলটিও লাল কিন্তু নিচে গ্যাপ দিয়ে খুলেছে (Gap Down)
    # ৩. তৃতীয় ক্যান্ডেলটি সবুজ হবে এবং সেটি দ্বিতীয় ক্যান্ডেলের ওপরে কিন্তু প্রথমটির নিচে থাকবে
    
    if c1.is_red and c2.is_red and c2.open < c1.low:
        if c3.is_green and c3.open > c2.close and c3.close < c1.close:
            return "BEARISH TRAP - Two Rabbits! বায়াররা ফাঁদে পড়েছে, মার্কেট আবার নিচে নামবে।"

    return "SCANNING - Looking for the rabbits"
def check_in_neck_pattern(c1, c2):
    # c1: বড় লাল ক্যান্ডেল (Strong Bearish)
    # c2: ছোট সবুজ ক্যান্ডেল যা নিচে গ্যাপ দিয়ে খুলেছে
    
    if c1.is_red and (c1.body > average_body):
        # c2 সবুজ হবে এবং এর ক্লোজ প্রাইস c1 এর লো এর কাছাকাছি হবে
        if c2.is_green and abs(c2.close - c1.low) < (c1.body * 0.1):
            return "WARNING - In-Neck Detected! এটা রিকভারি নয়, মার্কেট আরও নিচে পড়বে।"

    return "SCANNING - Trend is stable"
def check_morning_star(c1, c2, c3):
    # c1: বড় লাল ক্যান্ডেল (সেলাররা শেষ কামড় দিচ্ছে)
    # c2: ছোট বডির ক্যান্ডেল (সেলার আর বায়ারের মধ্যে দোটানা - Indecision)
    # c3: বড় সবুজ ক্যান্ডেল (বায়াররা চার্জ নিয়েছে)
    
    if c1.is_red and abs(c1.open - c1.close) > average_body:
        if abs(c2.open - c2.close) < (average_body * 0.3): # ছোট বডি
            if c3.is_green and c3.close > ((c1.open + c1.close) / 2):
                return "CRITICAL BUY - Morning Star! অন্ধকার শেষ, এবার মার্কেট আকাশে উড়বে।"
    
    return "SCANNING - Waiting for the star to rise"
def check_evening_star(c1, c2, c3):
    # c1: বড় সবুজ ক্যান্ডেল (বায়াররা খুব আত্মবিশ্বাসী)
    # c2: ছোট বডির ক্যান্ডেল (বায়ারদের ক্লান্তি শুরু)
    # c3: বড় লাল ক্যান্ডেল (সেলাররা মার্কেট দখল করে নিয়েছে)
    
    if c1.is_green and abs(c1.open - c1.close) > average_body:
        if abs(c2.open - c2.close) < (average_body * 0.3): # ছোট বডি (স্টার)
            if c3.is_red and c3.close < ((c1.open + c1.close) / 2):
                return "CRITICAL SELL - Evening Star! আলো নিভে গেছে, এবার মার্কেট নিচে আছড়ে পড়বে।"
    
    return "SCANNING - Market is still bright"
def check_breakout(current_candle, level, volume_spike):
    # Resistance Breakout
    if current_candle.close > level and volume_spike > average_volume:
        return "BREAKOUT DETECTED - বাঁধ ভেঙে গেছে! এবার বাই করো, মার্কেট রকেটের মতো ছুটবে।"

    # Support Breakdown
    elif current_candle.close < level and volume_spike > average_volume:
        return "BREAKDOWN DETECTED - পায়ের নিচ থেকে মাটি সরে গেছে! এবার সেল করো।"

    return "WAITING - Price is still inside the cage"
def check_fakeout(candle, level):
    # Resistance ব্রেকআউটের চেষ্টা করে ভেতরে ঢুকে পড়া
    if candle.high > level and candle.close < level:
        if (candle.high - level) > (abs(candle.open - candle.close) * 1.5):
            return "DANGER - Bull Trap! বায়ারদের ফাসিয়ে দেওয়া হয়েছে। এবার সেল করো।"

    # Support ব্রেকআউটের চেষ্টা করে ভেতরে ঢুকে পড়া
    elif candle.low < level and candle.close > level:
        if (level - candle.low) > (abs(candle.open - candle.close) * 1.5):
            return "DANGER - Bear Trap! সেলাররা ট্র্যাপে পড়েছে। এবার বাই করো।"

    return "SCANNING - Watching the breakout candle"
def check_dark_cloud_cover(prev_candle, current_candle):
    # ১. আগের ক্যান্ডেলটি শক্তিশালী সবুজ হতে হবে
    if prev_candle.is_green:
        # ২. বর্তমান ক্যান্ডেলটি আগের হাই-এর উপরে খুলবে (Gap Up)
        if current_candle.open > prev_candle.high:
            # ৩. কিন্তু ক্লোজ হবে আগের সবুজের বডির অন্তত ৫০% নিচে
            if current_candle.is_red and current_candle.close < (prev_candle.open + (prev_candle.body * 0.5)):
                return "CRITICAL SELL - Dark Cloud Cover! বায়ারদের দিন শেষ, এবার ধস নামবে।"

    return "SCANNING - Skies are still clear"
def check_piercing_line(prev_candle, current_candle):
    # ১. আগের ক্যান্ডেলটি শক্তিশালী লাল হতে হবে
    if prev_candle.is_red:
        # ২. বর্তমান ক্যান্ডেলটি আগের লো-এর নিচে খুলবে (Gap Down)
        if current_candle.open < prev_candle.low:
            # ৩. কিন্তু ক্লোজ হবে আগের লাল বডির অন্তত ৫০% উপরে
            if current_candle.is_green and current_candle.close > (prev_candle.close + (abs(prev_candle.open - prev_candle.close) * 0.5)):
                return "CRITICAL BUY - Piercing Line! সেলারদের দুর্গ ভেঙে গেছে, এবার মার্কেট উপরে উঠবে।"

    return "SCANNING - Sellers still in control"
def check_falling_three(c1, c2, c3, c4, c5):
    # c1: বড় লাল ক্যান্ডেল
    # c2, c3, c4: ছোট তিনটি সবুজ ক্যান্ডেল যা c1 এর রেঞ্জের ভেতরে আছে
    # c5: বড় লাল ক্যান্ডেল যা c1 এর লো ব্রেক করেছে
    
    if c1.is_red and (c1.body > average_body):
        if all(c.is_green and c.high < c1.high and c.low > c1.low for c in [c2, c3, c4]):
            if c5.is_red and c5.close < c1.close:
                return "TREND CONTINUATION - Falling Three! বায়ারদের শক্তি শেষ, মার্কেট আবার ধসে পড়বে।"

    return "SCANNING - Trend is developing"
def check_rising_three(c1, c2, c3, c4, c5):
    # c1: বড় সবুজ ক্যান্ডেল (Strong Bullish)
    # c2, c3, c4: ছোট তিনটি লাল ক্যান্ডেল যারা c1 এর রেঞ্জের ভেতরেই বন্দি
    # c5: আবার একটি বড় সবুজ ক্যান্ডেল যা c1 এর হাই ব্রেক করে উপরে ক্লোজ দেয়
    
    if c1.is_green and (c1.body > average_body):
        if all(c.is_red and c.high < c1.high and c.low > c1.low for c in [c2, c3, c4]):
            if c5.is_green and c5.close > c1.high:
                return "TREND EXPLOSION - Rising Three! বাঘ দুপা পিছিয়ে আবার লাফ দিয়েছে। বাই করো!"

    return "SCANNING - Market is taking a breather"
def check_matching_logic(c1, c2, trend):
    # Matching High (আপট্রেন্ডে রেজিস্ট্যান্সের ইঙ্গিত)
    if trend == "Uptrend" and c1.is_green and c2.is_green:
        if abs(c1.high - c2.high) < 0.0001: # প্রায় একই হাই
            return "RESISTANCE ALERT - Matching High! মার্কেট এই দেয়াল ভাঙতে পারছে না। সাবধান!"

    # Matching Low (ডাউনট্রেন্ডে সাপোর্টের ইঙ্গিত)
    if trend == "Downtrend" and c1.is_red and c2.is_red:
        if abs(c1.low - c2.low) < 0.0001: # প্রায় একই লো
            return "SUPPORT ALERT - Matching Low! নিচে নামার পথ বন্ধ। এখান থেকে বাউন্স করতে পারে।"

    return "SCANNING - Flow is smooth"
def check_bearish_strike(c1, c2, c3, c4):
    # পরপর তিনটি লাল ক্যান্ডেল যারা ক্রমান্বয়ে নিচের দিকে যাচ্ছে
    if c1.is_red and c2.is_red and c3.is_red:
        if c2.close < c1.close and c3.close < c2.close:
            # ৪ নম্বর ক্যান্ডেলটি হবে একটি বড় সবুজ যা আগের তিনটির ওপেন প্রাইসের উপরে ক্লোজ হবে
            if c4.is_green and c4.close > c1.open:
                return "CONTRA-ALERT - Bearish Three-Line Strike! এই সবুজ ক্যান্ডেলটি আসলে একটি ট্র্যাপ। মার্কেট আরও জোরে নিচে পড়বে।"

    return "SCANNING - Looking for the strike pattern"
def check_three_stars_south(c1, c2, c3):
    # ১. প্রথমটি বড় লাল ক্যান্ডেল এবং নিচের দিকে লম্বা উইক (Long Lower Wick)
    # ২. দ্বিতীয়টিও লাল, কিন্তু প্রথমটির রেঞ্জের ভেতরে এবং এর লো আগেরটির থেকে উপরে
    # ৩. তৃতীয়টি একটি ছোট লাল ক্যান্ডেল (Marubozu বা খুব ছোট উইক) এবং প্রথমটির রেঞ্জেই থাকে
    
    if c1.is_red and c2.is_red and c3.is_red:
        if c2.low > c1.low and c3.low > c2.low:
            if c3.body < c2.body and c2.body < c1.body:
                return "BULLISH SIGNAL - Three Stars in the South! সেলাররা ফুরিয়ে গেছে, এবার বায়াররা আসবে।"

    return "SCANNING - Sellers still have some juice"
def check_three_stars_south(c1, c2, c3):
    # ১. প্রথমটি বড় লাল ক্যান্ডেল এবং নিচের দিকে লম্বা উইক (Long Lower Wick)
    # ২. দ্বিতীয়টিও লাল, কিন্তু প্রথমটির রেঞ্জের ভেতরে এবং এর লো আগেরটির থেকে উপরে
    # ৩. তৃতীয়টি একটি ছোট লাল ক্যান্ডেল (Marubozu বা খুব ছোট উইক) এবং প্রথমটির রেঞ্জেই থাকে
    
    if c1.is_red and c2.is_red and c3.is_red:
        if c2.low > c1.low and c3.low > c2.low:
            if c3.body < c2.body and c2.body < c1.body:
                return "BULLISH SIGNAL - Three Stars in the South! সেলাররা ফুরিয়ে গেছে, এবার বায়াররা আসবে।"

    return "SCANNING - Sellers still have some juice"
def check_tweezer_top(c1, c2):
    # ১. প্রথমটি একটি শক্তিশালী সবুজ ক্যান্ডেল (সাধারণত)
    # ২. দ্বিতীয়টি যেকোনো রঙের হতে পারে (বেশিভাগ সময় লাল)
    # ৩. সবথেকে বড় শর্ত: দুটির হাই (High) একদম একই পয়েন্টে হতে হবে
    
    if abs(c1.high - c2.high) < 0.0001: # নিখুঁত হাই ম্যাচিং
        if c1.is_green and (c1.upper_wick < c1.body * 0.1): # ওপরের লেজ খুব ছোট
             return "REVERSAL ALERT - Tweezer Top! ওপরের দেয়ালে মাথা ঠুকে গেছে। এবার মার্কেট নিচে নামবে।"

    return "SCANNING - Looking for the tweezers"
def check_tweezer_bottom(c1, c2):
    # ১. প্রথমটি একটি শক্তিশালী লাল ক্যান্ডেল
    # ২. দ্বিতীয়টি সবুজ হলে সিগন্যাল বেশি শক্তিশালী হয়
    # ৩. সবথেকে বড় শর্ত: দুটির লো (Low) একদম একই পয়েন্টে হতে হবে
    
    if abs(c1.low - c2.low) < 0.0001: # নিখুঁত লো ম্যাচিং
        if c1.is_red and (c2.is_green):
             return "REVERSAL ALERT - Tweezer Bottom! নিচে শক্ত মেঝে তৈরি হয়েছে। এবার বাই করার সময়।"

    return "SCANNING - Sellers are still testing the floor"
def check_bullish_engulfing(prev_candle, current_candle):
    # ১. আগের ক্যান্ডেলটি লাল হতে হবে
    if prev_candle.is_red:
        # ২. বর্তমান ক্যান্ডেলটি সবুজ হবে এবং এটি আগের লাল ক্যান্ডেলকে পুরোপুরি ঢেকে দেবে
        if current_candle.is_green and current_candle.open <= prev_candle.close and current_candle.close > prev_candle.open:
            return "POWER BUY - Bullish Engulfing! বায়াররা সেলারদের গিলে ফেলেছে। এবার মার্কেট উপরে ছুটবে।"

    return "SCANNING - Sellers are still dominant"
def check_bearish_engulfing(prev_candle, current_candle):
    # ১. আগের ক্যান্ডেলটি সবুজ হতে হবে
    if prev_candle.is_green:
        # ২. বর্তমান ক্যান্ডেলটি লাল হবে এবং এটি আগের সবুজ ক্যান্ডেলকে পুরোপুরি ঢেকে দেবে
        if current_candle.is_red and current_candle.open >= prev_candle.close and current_candle.close < prev_candle.open:
            return "POWER SELL - Bearish Engulfing! সেলাররা বায়ারদের পিষে ফেলেছে। এবার মার্কেট ধসে পড়বে।"

    return "SCANNING - Buyers are still holding on"
def check_advance_block(c1, c2, c3):
    # তিনটি ক্যান্ডেলই সবুজ হবে এবং আগেরটির হাই ব্রেক করবে
    if c1.is_green and c2.is_green and c3.is_green:
        # শর্ত: ক্যান্ডেল যত উপরে যাচ্ছে, বডি তত ছোট হচ্ছে এবং ওপরের লেজ বড় হচ্ছে
        if c3.body < c2.body < c1.body:
            if c3.upper_wick > c3.body:
                return "CAUTION - Advance Block! বায়াররা ক্লান্ত। এবার ট্রেন্ড পাল্টাতে পারে।"
    
    return "SCANNING - Uptrend still has strength"
def check_descent_block(c1, c2, c3):
    # তিনটি ক্যান্ডেলই লাল হবে এবং আগেরটির লো ব্রেক করার চেষ্টা করবে
    if c1.is_red and c2.is_red and c3.is_red:
        # শর্ত: ক্যান্ডেল যত নিচে যাচ্ছে, বডি তত ছোট হচ্ছে এবং নিচের লেজ (Wick) বড় হচ্ছে
        if c3.body < c2.body < c1.body:
            if c3.lower_wick > c3.body:
                return "CAUTION - Descent Block! সেলাররা শক্তি হারাচ্ছে। এবার মার্কেট বাউন্স করবে।"
    
    return "SCANNING - Downtrend is still heavy"
def check_three_inside_logic(c1, c2, c3):
    # Three Inside Up (বুলিশ রিভার্সাল)
    if c1.is_red and c2.is_green and c2.close < c1.open and c2.open > c1.close:
        if c3.is_green and c3.close > c2.close:
            return "STRONG BUY - Three Inside Up! কনফার্মেশন মিলেছে, এবার ট্রেন্ড উপরে যাবে।"

    # Three Inside Down (বেয়ারিশ রিভার্সাল)
    if c1.is_green and c2.is_red and c2.close > c1.open and c2.open < c1.close:
        if c3.is_red and c3.close < c2.close:
            return "STRONG SELL - Three Inside Down! পতন নিশ্চিত, কনফার্মেশন ক্যান্ডেল তৈরি।"

    return "SCANNING - Waiting for confirmation"
def check_three_outside_up(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি হবে ছোট লাল (Bearish)
    # ২. দ্বিতীয় ক্যান্ডেলটি হবে বড় সবুজ যা প্রথমটিকে পুরোপুরি গিলে ফেলবে (Engulfing)
    if c1.is_red and c2.is_green and c2.open < c1.close and c2.close > c1.open:
        # ৩. তৃতীয় ক্যান্ডেলটি সবুজ হবে এবং ২ নম্বর ক্যান্ডেলের হাই-এর উপরে ক্লোজ দেবে
        if c3.is_green and c3.close > c2.close:
            return "ULTRA BUY - Three Outside Up! বায়াররা এখন অপ্রতিরোধ্য। নির্দ্বিধায় বাই করো।"

    return "SCANNING - Market is finding its rhythm"
def check_three_outside_down(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি ছোট সবুজ (Bullish)
    # ২. দ্বিতীয় ক্যান্ডেলটি বড় লাল যা প্রথমটিকে পুরোপুরি ঢেকে ফেলে (Engulfing)
    if c1.is_green and c2.is_red and c2.open > c1.close and c2.close < c1.open:
        # ৩. তৃতীয় ক্যান্ডেলটি লাল হবে এবং ২ নম্বর ক্যান্ডেলের লো-এর নিচে ক্লোজ দেবে
        if c3.is_red and c3.close < c2.close:
            return "ULTRA SELL - Three Outside Down! সেলাররা এখন মার্কেটের মালিক। বড় পতন আসছে।"

    return "SCANNING - Market is still indecisive"
def check_three_inside_bar(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি বড় (যেকোনো রঙ)
    # ২. দ্বিতীয় ক্যান্ডেলটি প্রথমটির বডির ভেতর (Inside Bar)
    # ৩. তৃতীয় ক্যান্ডেলটিও দ্বিতীয়টির বা প্রথমটির বডির ভেতর (Double Inside Bar)
    
    if abs(c1.open - c1.close) > average_body:
        if max(c2.open, c2.close) < max(c1.open, c1.close) and min(c2.open, c2.close) > min(c1.open, c1.close):
            if max(c3.open, c3.close) < max(c1.open, c1.close) and min(c3.open, c3.close) > min(c1.open, c1.close):
                return "VOLATILITY SQUEEZE - Three Inside Bar! মার্কেট ফেটে পড়ার অপেক্ষায়। যেদিকে ব্রেক করবে সেদিকেই ট্রেড নাও।"

    return "SCANNING - Market is moving normally"
def check_evening_star_doji(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি বড় এবং সবুজ
    if c1.is_green and c1.body > average_body:
        # ২. দ্বিতীয় ক্যান্ডেলটি একটি ডোজি এবং গ্যাপ-আপ দিয়ে খুলবে
        if is_doji(c2) and c2.open > c1.close:
            # ৩. তৃতীয় ক্যান্ডেলটি লাল হবে এবং প্রথম সবুজের অর্ধেকের নিচে ক্লোজ দেবে
            if c3.is_red and c3.close < (c1.open + c1.body * 0.5):
                return "CRITICAL REVERSAL - Evening Star Doji! আকাশের সূর্য ডুবে গেছে, এবার অন্ধকার (পতন) আসবে।"

    return "SCANNING - Trend is still intact"
def check_morning_star_doji(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি বড় এবং লাল
    if c1.is_red and c1.body > average_body:
        # ২. দ্বিতীয় ক্যান্ডেলটি একটি ডোজি এবং গ্যাপ-ডাউন দিয়ে খুলবে
        if is_doji(c2) and c2.open < c1.close:
            # ৩. তৃতীয় ক্যান্ডেলটি সবুজ হবে এবং প্রথম লালের অর্ধেকের উপরে ক্লোজ দেবে
            if c3.is_green and c3.close > (c1.close + c1.body * 0.5):
                return "CRITICAL BUY - Morning Star Doji! রাত পোহালো, এবার সূর্য (প্রাইস) উঠবে।"

    return "SCANNING - Market is still looking for bottom"
def check_bearish_harami_cross(c1, c2):
    # ১. প্রথম ক্যান্ডেলটি বড় এবং সবুজ (Bullish)
    if c1.is_green and c1.body > average_body:
        # ২. দ্বিতীয় ক্যান্ডেলটি একটি ডোজি (Dozi) এবং এটি প্রথমটির বডির ভেতরে থাকতে হবে
        if is_doji(c2) and c2.high < c1.high and c2.low > c1.low:
            return "DANGER ALERT - Bearish Harami Cross! বায়াররা স্থবির হয়ে গেছে। বড় পতন আসন্ন।"

    return "SCANNING - Trend is still moving up"
def check_bullish_harami_cross(c1, c2):
    # ১. প্রথম ক্যান্ডেলটি বড় এবং লাল (Bearish)
    if c1.is_red and c1.body > average_body:
        # ২. দ্বিতীয় ক্যান্ডেলটি একটি ডোজি (Doji) এবং এটি প্রথমটির বডির ভেতরে থাকতে হবে
        if is_doji(c2) and c2.high < c1.high and c2.low > c1.low:
            return "REVERSAL ALERT - Bullish Harami Cross! সেলাররা থমকে গেছে। বায়াররা এবার রাজত্ব নেবে।"

    return "SCANNING - Sellers are still in control"
def check_falling_window(prev_candle, current_candle):
    # শর্ত: আগের ক্যান্ডেলের লো (Low) বর্তমান ক্যান্ডেলের হাই (High) এর চেয়ে উপরে থাকতে হবে
    # অর্থাৎ দুটির মাঝে কোনো টাচ থাকবে না, মাঝখানে ফাঁকা জায়গা থাকবে।
    
    if prev_candle.low > current_candle.high:
        return "CRITICAL CONTINUATION - Falling Window! সেলাররা পাগলের মতো সেল করছে। মার্কেট আরও অনেক নিচে যাবে।"

    return "SCANNING - Looking for the window"
def check_rising_window(prev_candle, current_candle):
    # শর্ত: আগের ক্যান্ডেলের হাই (High) বর্তমান ক্যান্ডেলের লো (Low) এর চেয়ে নিচে থাকতে হবে
    # অর্থাৎ দুটির মাঝে আকাশ-পাতাল তফাত বা ফাঁকা জায়গা থাকবে।
    
    if prev_candle.high < current_candle.low:
        return "BULLISH CONTINUATION - Rising Window! বায়াররা রকেটে চড়েছে। মার্কেট আরও অনেক উপরে যাবে।"

    return "SCANNING - Waiting for the gap"
def check_abandoned_baby_top(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি বড় সবুজ
    # ২. দ্বিতীয় ক্যান্ডেলটি ছোট (ডোজি) যা গ্যাপ-আপ দিয়ে উপরে তৈরি হয় (কোনো টাচ নেই)
    # ৩. তৃতীয় ক্যান্ডেলটি লাল যা গ্যাপ-ডাউন দিয়ে নিচে খোলে (কোনো টাচ নেই)
    
    if c1.is_green and is_doji(c2) and c3.is_red:
        if c2.low > c1.high and c2.low > c3.high:
            return "DANGER - Abandoned Baby Top! মার্কেটের চূড়ায় সবাই আটকা পড়েছে। খাড়া পতন নিশ্চিত।"

    return "SCANNING - Looking for the lonely star"
def check_abandoned_baby_bottom(c1, c2, c3):
    # ১. প্রথম ক্যান্ডেলটি বড় লাল
    # ২. দ্বিতীয় ক্যান্ডেলটি ছোট (ডোজি) যা গ্যাপ-ডাউন দিয়ে নিচে তৈরি হয় (আগেরটির সাথে কোনো টাচ নেই)
    # ৩. তৃতীয় ক্যান্ডেলটি বড় সবুজ যা গ্যাপ-আপ দিয়ে উপরে খোলে (মাঝখানেরটির সাথে কোনো টাচ নেই)
    
    if c1.is_red and is_doji(c2) and c3.is_green:
        if c2.high < c1.low and c2.high < c3.low:
            return "ULTRA BUY - Abandoned Baby Bottom! পাতাল থেকে রকেট ছাড়ছে। এবার আকাশ ছোঁয়ার পালা।"

    return "SCANNING - Searching for the island of reversal"
def check_three_black_crows(c1, c2, c3):
    # ১. তিনটি ক্যান্ডেলই লাল এবং বড় হতে হবে
    if c1.is_red and c2.is_red and c3.is_red:
        # ২. প্রতিটি ক্যান্ডেল আগের ক্যান্ডেলের বডির ভেতর থেকে শুরু হবে
        if c1.close < c2.open < c1.open and c2.close < c3.open < c2.open:
            # ৩. প্রতিটি ক্যান্ডেল আগেরটির লো (Low) এর নিচে ক্লোজ হবে
            if c2.close < c1.low and c3.close < c2.low:
                return "CRITICAL SELL - Three Black Crows! আকাশে তিনটি শকুন (লাল ক্যান্ডেল) উড়ছে। ধ্বংস অনিবার্য।"

    return "SCANNING - Market is trying to breathe"
def check_three_white_soldiers(c1, c2, c3):
    # ১. তিনটি ক্যান্ডেলই সবুজ এবং শক্তিশালী হতে হবে
    if c1.is_green and c2.is_green and c3.is_green:
        # ২. প্রতিটি ক্যান্ডেল আগের ক্যান্ডেলের বডির ভেতর থেকে শুরু হবে (Open)
        if c1.open < c2.open < c1.close and c2.open < c3.open < c2.close:
            # ৩. প্রতিটি ক্যান্ডেল আগেরটির হাই (High) এর উপরে ক্লোজ হবে
            if c2.close > c1.high and c3.close > c2.high:
                return "AGGRESSIVE BUY - Three White Soldiers! তিন সৈন্যের পদধ্বনি শোনা যাচ্ছে। মার্কেট রকেটের মতো উপরে যাবে।"

    return "SCANNING - Sellers are still resisting"
def check_falling_three_methods(c1, c2, c3, c4, c5):
    # ১. প্রথম ক্যান্ডেলটি বড় লাল (Bearish)
    if c1.is_red and c1.body > average_body:
        # ২. মাঝখানের তিনটি ক্যান্ডেল (c2, c3, c4) হবে ছোট এবং সবুজ
        if all(c.is_green for c in [c2, c3, c4]):
            # ৩. এই তিনটি ক্যান্ডেল যেন প্রথম লালের হাই এবং লো-এর বাইরে না যায়
            if max(c2.high, c3.high, c4.high) < c1.open and min(c2.low, c3.low, c4.low) > c1.close:
                # ৪. পঞ্চম ক্যান্ডেলটি হবে বিশাল লাল যা আগের সবগুলোকে ছাপিয়ে নিচে ক্লোজ হবে
                if c5.is_red and c5.close < c1.close:
                    return "DEATH TRAP - Falling Three! বায়াররা ফাঁদে পড়েছে। মার্কেট ধসে পড়বে।"
    
    return "SCANNING - Sellers are taking a breath"
def check_rising_three_methods(c1, c2, c3, c4, c5):
    # ১. প্রথম ক্যান্ডেলটি বড় এবং সবুজ (Bullish)
    if c1.is_green and c1.body > average_body:
        # ২. মাঝখানের তিনটি ছোট ক্যান্ডেল (c2, c3, c4) হবে লাল
        if all(c.is_red for c in [c2, c3, c4]):
            # ৩. এই তিনটি ক্যান্ডেল যেন প্রথম সবুজের হাই এবং লো-এর ভেতরেই থাকে
            if max(c2.high, c3.high, c4.high) < c1.close and min(c2.low, c3.low, c4.low) > c1.open:
                # ৪. পঞ্চম ক্যান্ডেলটি হবে বিশাল সবুজ যা আগের সবগুলোকে ছাড়িয়ে উপরে ক্লোজ দেবে
                if c5.is_green and c5.close > c1.close:
                    return "TREND CONTINUATION - Rising Three! বায়াররা বিশ্রাম নিয়ে আবার ফিরেছে। মার্কেট আরও উপরে যাবে।"
    
    return "SCANNING - Market is consolidating"
def check_on_neck_pattern(prev_candle, current_candle):
    # ১. আগের ক্যান্ডেলটি বড় লাল (Bearish) হতে হবে
    if prev_candle.is_red and prev_candle.body > average_body:
        # ২. বর্তমান ক্যান্ডেলটি সবুজ হবে এবং গ্যাপ-ডাউন দিয়ে খুলবে
        if current_candle.is_green and current_candle.open < prev_candle.low:
            # ৩. কিন্তু সবুজ ক্যান্ডেলটি আগের লাল ক্যান্ডেলের লো-এর ঠিক কাছে গিয়ে ক্লোজ হবে
            if abs(current_candle.close - prev_candle.low) < small_margin:
                return "BEARISH CONTINUATION - On Neck! বায়াররা চেষ্টা করেও হার মেনেছে। মার্কেট আরও নিচে নামবে।"

    return "SCANNING - Market is struggling at the neck"
def check_downside_tasuki_gap(c1, c2, c3):
    # ১. প্রথম দুটি ক্যান্ডেল বড় লাল এবং তাদের মাঝে গ্যাপ (Window) থাকতে হবে
    if c1.is_red and c2.is_red and c2.open < c1.low:
        # ২. তৃতীয় ক্যান্ডেলটি হবে সবুজ
        if c3.is_green:
            # ৩. সবুজ ক্যান্ডেলটি ২ নম্বর ক্যান্ডেলের বডির ভেতর খুলবে 
            # এবং ১ ও ২ এর মাঝের গ্যাপের ভেতর ক্লোজ হবে (গ্যাপ পুরোপুরি ভরবে না)
            if c3.open > c2.close and c3.close < c1.low:
                return "SELL CONFIRMED - Tasuki Gap! বায়ারদের চেষ্টা ব্যর্থ। মার্কেট আবার আছড়ে পড়বে।"

    return "SCANNING - Market is testing the gap"
def check_upside_tasuki_gap(c1, c2, c3):
    # ১. প্রথম দুটি ক্যান্ডেল বড় সবুজ এবং তাদের মাঝে গ্যাপ (Window) থাকতে হবে
    if c1.is_green and c2.is_green and c2.open > c1.high:
        # ২. তৃতীয় ক্যান্ডেলটি হবে লাল
        if c3.is_red:
            # ৩. লাল ক্যান্ডেলটি ২ নম্বর ক্যান্ডেলের বডির ভেতর খুলবে 
            # এবং গ্যাপের ভেতর ক্লোজ হবে (কিন্তু গ্যাপ পুরোপুরি বন্ধ করবে না)
            if c3.open < c2.close and c3.close > c1.high:
                return "BUY CONFIRMED - Upside Tasuki Gap! বায়াররা শক্তি সঞ্চয় করছে। বড় লাফ আসন্ন।"

    return "SCANNING - Trend is taking a small break"
def check_matching_low(c1, c2):
    # ১. প্রথম ক্যান্ডেলটি বড় লাল (Bearish)
    if c1.is_red and c1.body > average_body:
        # ২. দ্বিতীয় ক্যান্ডেলটিও লাল হবে
        if c2.is_red:
            # ৩. কিন্তু দুটির ক্লোজিং প্রাইস একদম সমান বা প্রায় সমান হতে হবে
            if abs(c1.close - c2.close) < small_margin:
                return "REVERSAL ALERT - Matching Low! সেলাররা দেয়ালে পিঠ ঠেকে গেছে। এবার বায়ারদের পাল্টানোর পালা।"

    return "SCANNING - Sellers are still pushing down"
def check_matching_high(c1, c2):
    # ১. প্রথম ক্যান্ডেলটি বড় এবং সবুজ (Bullish)
    if c1.is_green and c1.body > average_body:
        # ২. দ্বিতীয় ক্যান্ডেলটিও সবুজ হবে
        if c2.is_green:
            # ৩. কিন্তু দুটির হাই (High) বা ক্লোজিং প্রাইস একদম সমান হতে হবে
            if abs(c1.close - c2.close) < small_margin:
                return "CEILING HIT - Matching High! বায়াররা কাঁচের দেয়ালে ধাক্কা খেয়েছে। এবার পতনের পালা।"

    return "SCANNING - Bulls are still trying to break the ceiling"
