values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def parse_roman_numeral(numeral):
    total = values[numeral[0]]

    for i in range(1, len(numeral)):
        if values[numeral[i-1]] < values[numeral[i]]:
            total += values[numeral[i]] - (2 * values[numeral[i-1]])
        else:
            total += values[numeral[i]]

    return total
