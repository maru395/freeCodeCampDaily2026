def get_bingo_letter(n):
    ranges = [
        (1, 15, "B"),
        (16, 30, "I"),
        (31, 45, "N"),
        (46, 60, "G"),
        (61, 75, "O")
    ]
    for low, high, letter in ranges:
            if low <= n <= high:
                return letter
    return n
