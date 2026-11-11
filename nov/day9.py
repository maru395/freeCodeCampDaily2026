def find_word(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    n = len(word)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]   # right, left, down, up

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != word[0]:
                continue
            for dr, dc in directions:
                end_r = r + dr * (n - 1)
                end_c = c + dc * (n - 1)

                # skip if the word would run off the grid
                if not (0 <= end_r < rows and 0 <= end_c < cols):
                    continue

                if all(matrix[r + dr * i][c + dc * i] == word[i] for i in range(n)):
                    return [[r, c], [end_r, end_c]]
