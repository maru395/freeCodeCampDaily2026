def sort_and_swap(arr):
    arr = sorted(arr)

    for i in range(2, len(arr) - 1, 3): # use 2 start so that we will access the 3rd index already, no need out of bound checl
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr
