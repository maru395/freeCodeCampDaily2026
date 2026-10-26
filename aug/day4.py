def calculate_handicap(scores, pars):
    n = len(scores)
    dif = 0
    for i in range(n):
        dif += scores[i] - pars[i]
    return round(dif/n, 1)
