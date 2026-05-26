def sum_of_differences(arr):
    sum_num = 0
    for i in range (1, len(arr)):
        sum_num += arr[i] - arr[i-1]
    return sum_num

