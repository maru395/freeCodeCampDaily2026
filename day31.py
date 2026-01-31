def get_sign(date_str):
    year, month, day = date_str.split("-")
    zodiac_signs = {
        "Aries":       ((3, 21),  (4, 19)),
        "Taurus":      ((4, 20),  (5, 20)),
        "Gemini":      ((5, 21),  (6, 20)),
        "Cancer":      ((6, 21),  (7, 22)),
        "Leo":         ((7, 23),  (8, 22)),
        "Virgo":       ((8, 23),  (9, 22)),
        "Libra":       ((9, 23),  (10, 22)),
        "Scorpio":     ((10, 23), (11, 21)),
        "Sagittarius": ((11, 22), (12, 21)),
        "Capricorn":   ((12, 22), (1, 19)),  # Note: Crosses year boundary
        "Aquarius":    ((1, 20),  (2, 18)),
        "Pisces":      ((2, 19),  (3, 20))
    }
    for sign, (start, end) in zodiac_signs.items():
        if start <= (int(month), int(day)) <= end:
            return sign
        elif start[0] > end[0]:
            if (int(month), int(day)) >= start or (int(month), int(day)) <= end:
                return sign
                
    return None
