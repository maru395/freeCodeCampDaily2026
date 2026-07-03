def connect_three(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    def check_line(cells):
        val = cells[0][0]
        if val != "" and all(v == val for v, _ in cells):
            return [val] + [pos for _, pos in cells]
        return None

    # Horizontal
    for r in range(rows):
        for c in range(cols - 2):
            cells = [(matrix[r][c + k], [r, c + k]) for k in range(3)]
            res = check_line(cells)
            if res:
                return res

    # Vertical
    for c in range(cols):
        for r in range(rows - 2):
            cells = [(matrix[r + k][c], [r + k, c]) for k in range(3)]
            res = check_line(cells)
            if res:
                return res

    # Diagonal: top-left to bottom-right
    for r in range(rows - 2):
        for c in range(cols - 2):
            cells = [(matrix[r + k][c + k], [r + k, c + k]) for k in range(3)]
            res = check_line(cells)
            if res:
                return res

    # Diagonal: top-right to bottom-left
    for r in range(rows - 2):
        for c in range(2, cols):
            cells = [(matrix[r + k][c - k], [r + k, c - k]) for k in range(3)]
            res = check_line(cells)
            if res:
                return res

    return []
