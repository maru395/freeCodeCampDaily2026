def find_differences(arr):
    new_arr = []
    for i in range(1, len(arr)):
        new_arr.append(arr[i]-arr[i-1])
    new_arr.append(0)
    return new_arr

# one liner code
# return [arr[i] - arr[i-1] for i in range(1, len(arr))] + [0]
