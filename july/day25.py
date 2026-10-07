def find_signal(grid):
    total_rows = len(grid)
    total_cols = len(grid[0])
    
    # 1. Find all towers and their distances
    towers = []
    for row in range(total_rows):
        for col in range(total_cols):
            if grid[row][col] > 0:
                reported_distance = grid[row][col]
                towers.append((row, col, reported_distance))
                
    # 2. Iterate through every cell in the grid to find the phone
    for row in range(total_rows):
        for col in range(total_cols):
            matches_all_towers = True
            
            for tower_row, tower_col, reported_distance in towers:
                row_distance = abs(row - tower_row)
                col_distance = abs(col - tower_col)
                
                # Check if the cell is along a straight line (H, V, or D) at the reported distance
                is_horizontal = (row_distance == 0 and col_distance == reported_distance)
                is_vertical = (col_distance == 0 and row_distance == reported_distance)
                is_diagonal = (row_distance == col_distance and row_distance == reported_distance)
                
                if not (is_horizontal or is_vertical or is_diagonal):
                    matches_all_towers = False
                    break
            
            # Since there is exactly one solution, return it as soon as it's found
            if matches_all_towers:
                return [row, col]
