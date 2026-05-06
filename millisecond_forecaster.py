def forecast_tick_movement(ticks):
    # মাইক্রো-মুভমেন্ট এনালাইসিস
    last_tick = ticks[-1]
    second_last = ticks[-2]
    velocity = last_tick - second_last
    return "UP_TICK" if velocity > 0 else "DOWN_TICK"
