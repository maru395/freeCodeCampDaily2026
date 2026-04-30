def is_in_crossword(char):
    grid = [
        "01000001",
        "01101111",
        "01000100",
        "01100101",
        "01010010",
        "01010100",
        "01101000",
        "10101110"
    ]

    target = format(ord(char), "08b")

    # check rows (both directions)
    for row in grid:
        if target in row or target[::-1] in row:
            return True

    # check columns (both directions)
    for col in range(8):
        column = "".join(grid[row][col] for row in range(8))
        if target in column or target[::-1] in column:
            return True

    return False

# faster approach for this specific problem
# def is_in_crossword(char):
#     decimal = {65, 111, 68, 101, 82, 84, 104, 174, 130, 246, 34, 166, 74, 42, 22, 117, 1, 254, 83, 12, 67, 117, 73, 208, 128, 127, 202, 48, 194, 174, 146, 11}
#     return ord(char) in decimal
