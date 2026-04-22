def parse_pos(pos):
    col = ord(pos[0].upper()) - ord('A')  # 'A' = 0, 'B' = 1, etc.
    row = int(pos[1]) - 1                 # '1' = 0, '2' = 1, etc.
    return (row, col)

def rook_bishop_attack(rook, bishop):
    r = parse_pos(rook)
    b = parse_pos(bishop)

    if r[0] == b[0] or r[1] == b[1]:
        return "rook"
    elif abs(r[0] - b[0]) == abs(r[1] - b[1]):
        return "bishop"
    else:
        return "neither"
