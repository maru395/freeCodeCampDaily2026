def invert_matrix(matrix):
    flatten = [x for subset in matrix for x in subset]
    val = list(set(flatten))
    
    return [[val[1] if element == val[0] else val[0] for element in subset] for subset in matrix]
