from collections import deque

def bucket_fill(grid, target_color):
    rows, cols = len(grid), len(grid[0])
    steps = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != target_color:
                original = grid[r][c]
                steps += 1
                grid[r][c] = target_color
                queue = deque([(r, c)])

                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original:
                            grid[nr][nc] = target_color
                            queue.append((nr, nc))

    return steps

