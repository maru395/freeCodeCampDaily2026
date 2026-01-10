def tic_tac_toe(board): # since this is a 3x3 array hardcode is faster
    # rows
    if board[0][0] == board[0][1] == board[0][2]:
        return "O win" if board[0][0] == "O" else "X win"
    if board[1][0] == board[1][1] == board[1][2]:
        return "O win" if board[1][0] == "O" else "X win"
    if board[2][0] == board[2][1] == board[2][2]:
        return "O win" if board[2][0] == "O" else "X win"
    # columns
    if board[0][0] == board[1][0] == board[2][0]:
        return "O win" if board[0][0] == "O" else "X win"
    if board[0][1] == board[1][1] == board[2][1]:
        return "O win" if board[0][1] == "O" else "X win"
    if board[0][2] == board[1][2] == board[2][2]:
        return "O win" if board[0][2] == "O" else "X win"
    # diags
    if board[0][0] == board[1][1] == board[2][2]:
        return "O win" if board[0][0] == "O" else "X win"
    if board[0][2] == board[1][1] == board[2][0]:
        return "O win" if board[0][2] == "O" else "X win"
    else: # defualt
        return "tie"
