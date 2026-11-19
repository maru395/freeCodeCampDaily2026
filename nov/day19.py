def convert(heading):
    heading = heading.lstrip()

    level = 0
    while level < len(heading) and heading[level] == "#":
        level += 1

    if level == 0 or level > 6:
        return "Invalid format"

    rest = heading[level:]
    if not rest.startswith(" "):
        return "Invalid format"

    text = rest.strip()
    if not text:
        return "Invalid format"

    return f"<h{level}>{text}</h{level}>"
