def get_meeting_time(availability):
    num_people = len(availability)
    
    # Start a pointer at 0 for every person
    ptrs = [0] * num_people
    
    # Loop as long as NO ONE has run out of time slots
    while all(ptrs[i] < len(availability[i]) for i in range(num_people)):
        
        # Get the current interval for every person
        current_intervals = [availability[i][ptrs[i]] for i in range(num_people)]
        
        # Find the global overlap window across ALL people
        g_start = max(interval[0] for interval in current_intervals)
        g_end = min(interval[1] for interval in current_intervals)
        
        # If the highest start is less than the lowest end, EVERYONE overlaps!
        if g_start < g_end:
            return g_start
            
        # Otherwise, find who is lagging behind (whoever ends earliest)
        # and move their pointer forward.
        for i in range(num_people):
            if availability[i][ptrs[i]][1] == g_end:
                ptrs[i] += 1
                
    return "None"
