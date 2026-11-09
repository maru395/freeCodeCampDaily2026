def battle(our_team, opponent):
    diff = 0
    for a, b in zip(our_team.split(), opponent.split()):
        va = sum((ord(c) - 64) * 2 if c.isupper() else ord(c) - 96 for c in a)
        vb = sum((ord(c) - 64) * 2 if c.isupper() else ord(c) - 96 for c in b)
        diff += (va > vb) - (va < vb)

    if diff > 0:
        return "We win"
    if diff < 0:
        return "We lose"
    return "Draw"
