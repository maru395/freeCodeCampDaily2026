from collections import Counter

def fix_prank_number(arr):
    if len(arr) < 2:
        return arr

    # 1. Calculate all gaps between adjacent numbers
    gaps = [(arr[i] - arr[i-1]) for i in range(1, len(arr))]
    
    # 2. Find the most common gap (this is our "true" step)
    counts = Counter(gaps)
    # most_common(1) returns a list like [(value, count)]
    step = counts.most_common(1)[0][0]

    # 3. Find a trusted anchor: the first index where the gap matches the correct step
    # If gaps[i] is correct, then arr[i] and arr[i+1] are both "trusted"
    anchor_idx = 0
    for i in range(len(gaps)):
        if gaps[i] == step:
            anchor_idx = i # We can trust arr[anchor_idx]
            break
    
    # 4. Rebuild the array from the anchor outward
    result = [0] * len(arr)
    result[anchor_idx] = arr[anchor_idx]
    
    # Fill backwards
    for i in range(anchor_idx - 1, -1, -1):
        result[i] = result[i+1] - step
        
    # Fill forwards
    for i in range(anchor_idx + 1, len(arr)):
        result[i] = result[i-1] + step
    
    return result
