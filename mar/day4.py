def card_values(cards):
    value = [i[:-1] for i in cards]
    final = []
    for v in value:
        if v == "A":
            final.append(1)
        elif v in "JQK":
            final.append(10)
        else:
            final.append(int(v))
    return final

""" def card_values(cards):
    values = {"A": 1, "J": 10, "Q": 10, "K": 10}
    return [values.get(c[:-1], int(c[:-1])) for c in cards] """
