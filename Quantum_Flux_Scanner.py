# Module 1: Quantum Flux Scanner
# Purpose: High-Frequency Micro-Momentum Detection

import numpy as np

def calculate_quantum_flux(data_stream):
    """
    এটি মার্কেটের নয়েজ ফিল্টার করে আসল মোমেন্টাম খুঁজে বের করে।
    """
    prices = np.array(data_stream)
    velocity = np.diff(prices) # দাম পরিবর্তনের গতি
    acceleration = np.diff(velocity) # গতির পরিবর্তন
    
    # যদি গতি এবং ত্বরণ একই দিকে তীব্র হয়, তবেই এটি 'True Flux'
    if acceleration[-1] > 0 and velocity[-1] > 0:
        return "BULLISH_STORM"
    elif acceleration[-1] < 0 and velocity[-1] < 0:
        return "BEARISH_STORM"
    return "STAGNANT"
