def letter_distance(str1, str2):
    n = 0
    for i in range(len(str1)):
        straight_distance = abs(ord(str1[i]) - ord(str2[i]))
        wrap_distance = 26 - straight_distance
        n += min(straight_distance, wrap_distance)
    return n
