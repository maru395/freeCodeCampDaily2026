def find_sum(arr, target):
    n = len(arr)

    def backtrack(start, current, total):
        # valid subset (at least 2 elements)
        if total == target and len(current) >= 2:
            return current

        if total > target:
            return None

        for i in range(start, n):
            res = backtrack(i + 1, current + [arr[i]], total + arr[i])
            if res:
                return res

        return None

    result = backtrack(0, [], 0)
    return result if result else "Sum not found"
