import math
from datetime import datetime, timedelta

def calculate_parking_fee(park_time, pickup_time):
    fmt = '%H:%M'
    
    p_time = datetime.strptime(park_time, fmt)
    u_time = datetime.strptime(pickup_time, fmt)
    
    passed_midnight = u_time < p_time
    
    if passed_midnight:
        diff = (u_time + timedelta(days=1)) - p_time
    else:
        diff = u_time - p_time
        
    total_minutes = diff.total_seconds() / 60
    billable_hours = math.ceil(total_minutes / 60)
    
    if billable_hours <= 1:
        base_cost = 5
    else:
        base_cost = billable_hours * 3
        
    total_cost = base_cost + (10 if passed_midnight else 0)
    
    return total_cost
