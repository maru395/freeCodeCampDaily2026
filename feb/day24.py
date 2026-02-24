import numpy as np

def count_business_days(start, end):
    return np.busday_count(start, end)

print(count_business_days("2026-02-24", "2026-02-28"))
