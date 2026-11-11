def can_post(message):
    characters = len(message)
    if characters <= 40:
        return "short post"
    elif characters > 40 and characters <= 80:
        return "long post"
    return "invalid post"
