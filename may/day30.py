from collections import Counter

RANK_ORDER = "23456789TJQKA"

def get_best_hand(cards: list[str]) -> str:
    ranks = [c[0] for c in cards]
    suits = [c[1] for c in cards]
    values = sorted(RANK_ORDER.index(r) for r in ranks)
    counts = sorted(Counter(ranks).values(), reverse=True)

    flush    = len(set(suits)) == 1
    royal    = set(ranks) == {"A", "K", "Q", "J", "T"}
    straight = (values[-1] - values[0] == 4 and len(set(values)) == 5) \
               or set(values) == {0, 1, 2, 3, 12}  # Ace-low: A,2,3,4,5

    if flush and royal:       return "Royal Flush"
    if flush and straight:    return "Straight Flush"
    if counts == [4, 1]:      return "Four of a Kind"
    if counts == [3, 2]:      return "Full House"
    if flush:                 return "Flush"
    if straight:              return "Straight"
    if counts == [3, 1, 1]:   return "Three of a Kind"
    if counts == [2, 2, 1]:   return "Two Pair"
    if counts == [2, 1, 1, 1]:return "Pair"
    return "High Card"
