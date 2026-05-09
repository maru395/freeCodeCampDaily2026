def transpose(matrix):
    row = len(matrix)
    col =  len(matrix[0])

    # create new matrix format
    new_matrix = [[0] * row for _ in range(col)]
    
    for r in range(row):
        for c in range(col):
            new_matrix[c][r] = matrix[r][c]

    return new_matrix
