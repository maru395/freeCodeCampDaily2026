def detect_roast(beans):
    sum = 0
    for x in beans:
        sum += 1 if x == "'" else 2 if x == "-" else 3
    ave = sum / len(beans)
    return "Light" if ave < 1.75 else "Medium" if 1.75 <= ave <= 2.5 else "Dark"
