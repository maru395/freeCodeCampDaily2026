def find_missing_numbers(arr): 
    # set for faster lookup
    present = set(arr)
    # get max and min for the loop and then check if in present
    return [i for i in range(min(present), max(present) + 1) if i not in present]
