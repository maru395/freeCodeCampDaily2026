# two sum using hashmap
def find_target(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        compliment = target - num
        if compliment in seen:
            return [seen[compliment], i]
        seen[num] = i
    return 'Target not found'
