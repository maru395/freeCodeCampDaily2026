def find_pawn_moves(position):
    moves = [
        (0,-1)
    ]
    if "2" in position:
        moves.append((0,-2))
    valid_moves = []
    def square_to_xy(square):
        files = "ABCDEFGH"
        file = square[0].upper()   
        rank = int(square[1])      
        x = files.index(file)
        y = 8 - rank
        return x, y
    x, y = square_to_xy(position)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            valid_moves.append((nx, ny))
    def xy_to_square(x, y):
        files = "ABCDEFGH"
        return f"{files[x]}{8 - y}"
    return [xy_to_square(nx, ny) for nx, ny in valid_moves]
