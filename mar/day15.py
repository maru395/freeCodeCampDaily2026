def get_captured_value(pieces):
    max = 39
    piece_values = {
        "P": 1,
        "N": 3,
        "B": 3,
        "R": 5,
        "Q": 9,
        "K": 0
    }
    if "K" not in pieces:
        return "Checkmate"
    for p in pieces:
        max -= piece_values.get(p, 0)
    return max

print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))
