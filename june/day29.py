def get_mood(genre, bpm):
    table = {
        "classical":  [(60, 109, "focus"), (110, 180, "happy")],
        "electronic": [(60, 89, "focus"), (90, 134, "happy"), (135, 180, "hype")],
        "pop":        [(60, 180, "happy")],
        "rock":       [(60, 129, "happy"), (130, 180, "hype")],
    }

    for lo, hi, mood in table.get(genre, []):
        if lo <= bpm <= hi:
            return mood
    return None
