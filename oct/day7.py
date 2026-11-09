def find_landing_spot(matrix):
    rows, cols = len(matrix), len(matrix[0])
    best_total = float("inf")
    best_spot = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                continue

            total = 0
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    total += matrix[nr][nc]

            if total < best_total:
                best_total = total
                best_spot = [r, c]

    return best_spot
