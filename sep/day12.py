def too_much_screen_time(hours):
    window = []
    total = 0
    for h in hours:
        # case 1
        if h >= 10:
            return True
        
        window.append(h)
        if len(window) > 3:
            window.pop(0)
        
        # case 2
        if sum(window)/3 >= 8:
            return True
        
        total += h
    
    return total/7 >= 6
