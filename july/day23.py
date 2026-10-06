def play_game(p1, p2):
    s_p1 = 0
    s_p2 = 0

    for i in range(len(p1)):
        if p1[i] == "C" and p1[i] == p2[i]:
            s_p1 += 3
            s_p2 += 3
        elif p1[i] == "D" and p1[i] == p2[i]:
            s_p1 += 1
            s_p2 += 1
        elif p1[i] == "D" and p1[i] != p2[i]:
            s_p1 += 5
        else:
            s_p2 += 5
            
    return [s_p1, s_p2]
