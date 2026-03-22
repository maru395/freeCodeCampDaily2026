def rotate(matrix):
    # Rotate 90° clockwise
    return [list(row) for row in zip(*matrix[::-1])]

def is_marker(matrix, coords):
    return all(matrix[i][j] == '1' for i, j in coords)

def decode_qr(qr_code):
    # Convert to list of lists if needed
    qr_code = [list(row) for row in qr_code]
    n = 6

    for _ in range(4):  # try all rotations
        # Define corner 2x2 blocks
        top_left = [(0,0),(0,1),(1,0),(1,1)]
        top_right = [(0,n-2),(0,n-1),(1,n-2),(1,n-1)]
        bottom_left = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

        # Check correct orientation
        if (is_marker(qr_code, top_left) and
            is_marker(qr_code, top_right) and
            is_marker(qr_code, bottom_left)):

            # Exclude marker cells
            excluded = set(top_left + top_right + bottom_left)

            result = []
            for i in range(n):
                for j in range(n):
                    if (i, j) not in excluded:
                        result.append(qr_code[i][j])

            return "".join(result)

        # Rotate and try again
        qr_code = rotate(qr_code)

    return ""  # should never happen
