def space_jam(s):
    return "  ".join(c.upper() for c in s if not c.isspace()).strip()
