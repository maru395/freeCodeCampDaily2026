def largest_difference(skater1, skater2):
    temp = skater1[0] - skater2[0]
    best_lap = 1
    for i in range(len(skater1)):
        if abs(skater1[i] - skater2[i]) > temp:
            temp = abs(skater1[i] - skater2[i])
            best_lap = i + 1
    return best_lap
