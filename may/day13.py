def find_offender(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            if i >= 2 and arr[i] < arr[i-2]:
                return i   
            return i - 1   
