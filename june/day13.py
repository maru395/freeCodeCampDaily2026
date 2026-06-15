def get_zone_violations(grid):
    if not grid or not grid[0]:
        return []
        
    violators = set() # Using a set avoids adding the same coordinate pair twice
    
    # Map out what a zone CANNOT be next to
    violation_rules = {
        "i": ["R", "I"],
        "A": ["C"],
        "R": ["i", "C"],
        "I": ["i"],
        "C": ["R", "A"],
    }
    
    rows = len(grid)
    cols = len(grid[0])
    boundary = [(-1,0), (0,1), (1,0), (0,-1)] # Clockwise: Up, Right, Down, Left
    
    for i in range(rows):
        for j in range(cols):
            current_zone = grid[i][j]
            
            # If the current space is empty, skip checking it
            if current_zone == "" or current_zone not in violation_rules:
                continue
                
            for direction_i, direction_j in boundary:
                ni, nj = direction_i + i, direction_j + j
                
                # Boundary safety check
                if 0 <= ni < rows and 0 <= nj < cols:
                    neighbor_zone = grid[ni][nj]
                    
                    # Check if the neighbor zone is an illegal zone for the current zone
                    if neighbor_zone in violation_rules[current_zone]:
                        # Add the violating NEIGHBOR's coordinates to our set
                        violators.add((ni, nj)) 
                        
    # Convert set of tuples back to a list of lists to match your format
    return [list(coord) for coord in violators]

# Test cases
print(get_zone_violations([["R", "C"], ["", "C"]]))
