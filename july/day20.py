def is_golden_ratio(a, b):
    ratio = max(a, b) / min(a, b)
    
    return 1.608 <= ratio <= 1.628
    
