from collections import deque

def shift_array(arr, n):
    mdeque = deque(arr)
    mdeque.rotate(-n)
    return list(mdeque)
