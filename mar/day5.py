# to review
def smallest_gap(s):
    last_seen = {}
    min_gap = float('inf')
    result = ""

    for i, c in enumerate(s):
        if c in last_seen:
            gap = i - last_seen[c] - 1
            if gap < min_gap:
                min_gap = gap
                result = s[last_seen[c] + 1:i]
        last_seen[c] = i

    return result
