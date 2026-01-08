def is_sorted(arr):
  if all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)):
    return "ascending"
  elif all(arr[i] >= arr[i+1] for i in range(len(arr) - 1)):
    return "descending"
  else:
    return "not sorted"
