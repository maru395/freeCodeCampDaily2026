# to review
def trail_traversal(trail):
    rows, cols = len(trail), len(trail[0])

    # find starting position
    for r in range(rows):
        for c in range(cols):
            if trail[r][c] == "C":
                start = (r, c)

    # directions: (row_change, col_change, move_letter)
    dirs = [
        (0, 1, "R"),
        (1, 0, "D"),
        (0, -1, "L"),
        (-1, 0, "U")
    ]

    r, c = start
    prev = None
    moves = ""

    while trail[r][c] != "G":
        for dr, dc, move in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) != prev and trail[nr][nc] in ("T", "G"):
                    moves += move
                    prev = (r, c)
                    r, c = nr, nc
                    break

    return moves
