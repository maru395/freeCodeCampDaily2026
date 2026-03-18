import re

def largest_number(s):
    result = re.split(r"[,!?:;]", s)
    results = [float(x) for x in result]
    return max(results)
