def truncate_text(s):
    # Character width definitions
    widths = {
        1: "ilI.",
        2: "fjrt ",
        3: "abcdeghkmnopqrstuvwxyzJL",
        4: "ABCDEFGHKMNOPQRSTUVWXYZ"
    }

    # Build lookup dictionary
    char_width = {}
    for w, chars in widths.items():
        for c in chars:
            char_width[c] = w

    def get_width(c):
        return char_width.get(c, 3)  # default width = 3

    ellipsis_width = 1 * 2  # ".." width = 2
    current_width = 0
    result = []

    # Add letters until next letter + ellipsis would exceed 60
    for c in s:
        w = get_width(c)
        if current_width + w + ellipsis_width > 60:
            break
        result.append(c)
        current_width += w

    # Only add ".." if we truncated
    if len(result) < len(s):
        result = "".join(result) + ".."
    else:
        result = "".join(result)
    return result
