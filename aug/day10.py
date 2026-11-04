from collections import deque

def bucket_fill(grid, target_color):
    row_count, col_count = len(grid), len(grid[0])

    # Tuples are hashable, so a whole grid can go in the "visited" set.
    start_state = tuple(tuple(row) for row in grid)

    def find_regions(state):
        # A region is a group of touching cells with the same color.
        # One bucket click always recolors exactly one whole region.
        seen = set()
        regions = []
        for row in range(row_count):
            for col in range(col_count):
                if (row, col) in seen:
                    continue
                color = state[row][col]
                cells = [(row, col)]
                seen.add((row, col))
                queue = deque([(row, col)])
                while queue:
                    current_row, current_col = queue.popleft()
                    for next_row, next_col in ((current_row - 1, current_col),
                                               (current_row + 1, current_col),
                                               (current_row, current_col - 1),
                                               (current_row, current_col + 1)):
                        if (0 <= next_row < row_count and 0 <= next_col < col_count
                                and (next_row, next_col) not in seen
                                and state[next_row][next_col] == color):
                            seen.add((next_row, next_col))
                            cells.append((next_row, next_col))
                            queue.append((next_row, next_col))
                regions.append((color, cells))
        return regions

    def touching_colors(state, cells, own_color):
        # Colors of the cells bordering this region.
        colors = set()
        for row, col in cells:
            for next_row, next_col in ((row - 1, col), (row + 1, col),
                                       (row, col - 1), (row, col + 1)):
                if 0 <= next_row < row_count and 0 <= next_col < col_count:
                    if state[next_row][next_col] != own_color:
                        colors.add(state[next_row][next_col])
        return colors

    def is_goal(state):
        return all(cell == target_color for row in state for cell in row)

    # BFS over whole grids: each click is one move, so the first time we
    # reach the goal is guaranteed to be the minimum number of clicks.
    visited = {start_state}
    queue = deque([(start_state, 0)])

    while queue:
        state, clicks = queue.popleft()
        if is_goal(state):
            return clicks

        for color, cells in find_regions(state):
            # Only try colors that can help: a neighbor's color (merges
            # regions) or the target color. Other colors would just waste
            # a click, and skipping them keeps the search small.
            for new_color in touching_colors(state, cells, color) | {target_color}:
                if new_color == color:
                    continue
                new_grid = [list(row) for row in state]
                for row, col in cells:
                    new_grid[row][col] = new_color
                new_state = tuple(tuple(row) for row in new_grid)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, clicks + 1))

    return -1
