def elevator_stops(current_floor, stops):
    sorted_stops = sorted(stops)
    
    lower_floors = [f for f in sorted_stops if f < current_floor]
    upper_floors = [f for f in sorted_stops if f > current_floor]
    
    if not lower_floors:
        up = True
    elif not upper_floors:
        up = False
    else:
        closest_lower = lower_floors[-1] 
        closest_upper = upper_floors[0]  
        
        if abs(closest_lower - current_floor) <= abs(closest_upper - current_floor):
            up = False
        else:
            up = True
a
    if up:
        return upper_floors + sorted(lower_floors, reverse=True)
    else:
        return sorted(lower_floors, reverse=True) + upper_floors
