def golf_score(par, strokes):
    if strokes == 1:
        return "hole in one!"
    elif par - 2 == strokes:
        return "eagle"
    elif par - 1 == strokes:
        return "birdie"
    elif par == strokes:
        return "par"
    elif par + 1 == strokes:
        return "bogey"
    elif par + 2 == strokes:
        return "double bogey"
    else:
        return "go home"
