def is_flat(arr):
    for i in arr:
        if isinstance(i, list):
            return False
    return True
    # return not any(isinstance(i, list) for i in arr)
