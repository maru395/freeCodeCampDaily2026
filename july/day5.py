from collections import deque

def bucket_fill(grid, pos, new_value):
    # helper function
    def get_connected_cells(matrix, start_row, start_col):
    # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        target_value = matrix[start_row][start_col]
        
        # Track visited cells to prevent infinite loops
        visited = {(start_row, start_col)}
        queue = deque([(start_row, start_col)])
        connected_cells = []
        
        # 4 possible movement directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            connected_cells.append((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Check if it matches the target value and hasn't been visited yet
                    if (nr, nc) not in visited and matrix[nr][nc] == target_value:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return connected_cells

    def update_single_cell(matrix, coordinate, new_value):
        if not matrix or not matrix[0]:
            return False
            
        row, col = coordinate
        rows, cols = len(matrix), len(matrix[0])
        matrix[row][col] = new_value

    cells = get_connected_cells(grid, pos[0], pos[1])
    for c in cells:
        update_single_cell(grid, c, new_value)
    
    return grid
