def get_contrast_rating(ratio, is_large_text):
    d = float(ratio)
    if not is_large_text:
        if d >= 7.0:
            return "AAA"
        elif d >= 4.5:
            return "AA"
        else:
            return "Fail"
    else:
        if d >= 4.5:
            return "AAA"
        elif d >= 3.0:
            return "AA"
        else:
            return "Fail"
