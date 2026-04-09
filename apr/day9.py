def get_next_bingo_number(bingo_num):
    ranges = [
        ("B", 1,  15),
        ("I", 16, 30),
        ("N", 31, 45),
        ("G", 46, 60),
        ("O", 61, 75),
    ]

    letter = bingo_num[0].upper()
    number = int(bingo_num[1:])

    current_index = next(i for i, (l, _, _) in enumerate(ranges) if l == letter)
    _, start, end = ranges[current_index]

    if number < end:
        return f"{letter}{number + 1}"               # still within same letter

    next_index = (current_index + 1) % len(ranges)  # advance to next letter
    next_letter, next_start, _ = ranges[next_index]
    return f"{next_letter}{next_start}"              # first number of next letter
