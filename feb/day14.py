def get_difficulty(track):
    score = 0
    temp = track[0]
    for i in track:
        if i == "S":
            score += 0
            temp = i
        elif i != temp and temp != "S":
            score += 15
            temp = i
        else:
            score += 5
            temp = i
    return score
