from datetime import datetime

def digital_detox(logs):
    fmt = "%Y-%m-%d %H:%M:%S"
    logins = sorted([datetime.strptime(date, fmt) for date in date_list])
    
    # Check every entry in the sorted history
    for i in range(len(logins)):
        
        # RULE 1: No more than once within any four-hour period
        if i > 0:
            diff = logins[i] - logins[i-1]
            if diff.total_seconds() < 14400: 
                return False

        # RULE 2: No more than 2 times on any single day
        if i >= 2:
            if logins[i].date() == logins[i-2].date():
                return False
                
    return True
