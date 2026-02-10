import datetime

def get_relative_results(results):
    time_values = []
    time_format = []
    
    # to seconds
    for i in results:
        h, m, s = i.split(":")
        time_values.append(int(h) *3600 + int(m) *60 + int(s))
    
    # find the minimum and subract it to the rest
    fastest = sorted(time_values)[0]
    for i in range(len(time_values)):
        time_values[i] = time_values[i] - fastest
    
    # convert the seconds into H:MM:SS format
    for i in range(len(time_values)):
        time_format.append(f"+{str(datetime.timedelta(seconds=time_values[i]))}")
    
    return time_format

# to refine return by checking 0 using cases
