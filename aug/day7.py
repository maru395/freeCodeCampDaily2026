def is_valid_nonogram(clue, cells):
    groups = []
    current = []

    for n in cells:
        if n == 0:
            if current:
                groups.append(current)
            current = []
        else:
            current.append(n)

    if current:
        groups.append(current)

    if len(groups) != len(clue):
        return False

    for i, c in enumerate(clue):
        if c != len(groups[i]):
            return False
    return True
