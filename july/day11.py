from collections import Counter

def five_dice(dice):
    counts = Counter(dice)
    freq = sorted(counts.values(), reverse=True)   # e.g. [3,2] for full house
    distinct = set(dice)

    # Straight checks (based on the actual values present, not just counts)
    large_straights = [{1,2,3,4,5}, {2,3,4,5,6}]
    small_straights = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]

    if distinct in large_straights:
        return "large straight"

    if freq[0] == 5:
        return "five of a kind"
    if freq[0] == 4:
        return "four of a kind"
    if freq[0] == 3 and freq[1] == 2:
        return "full house"

    if any(s.issubset(distinct) for s in small_straights):
        return "small straight"

    if freq[0] == 3:
        return "three of a kind"
    if freq.count(2) == 2:
        return "two pair"
    if freq[0] == 2:
        return "pair"

    return "no pair"

