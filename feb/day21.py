# to review
def score_curling(house):
    R = []
    Y = []
    center = (2, 2)

    for i in range(len(house)):
        for j in range(len(house[i])):
            if house[i][j] == "R":
                dist = (i - 2) ** 2 + (j - 2) ** 2
                R.append(dist)
            elif house[i][j] == "Y":
                dist = (i - 2) ** 2 + (j - 2) ** 2
                Y.append(dist)

    if not R and not Y:
        return "No points awarded"

    R.sort()
    Y.sort()

    if not R:
        return f"Y: {len(Y)}"
    if not Y:
        return f"R: {len(R)}"

    if R[0] < Y[0]:
        # R scores
        closest_Y = Y[0]
        points = sum(1 for d in R if d < closest_Y)
        return f"R: {points}"
    elif Y[0] < R[0]:
        # Y scores
        closest_R = R[0]
        points = sum(1 for d in Y if d < closest_R)
        return f"Y: {points}"
    else:
        return "No points awarded"
