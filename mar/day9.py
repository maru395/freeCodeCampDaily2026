def is_valid_hsl(hsl):
    for i in range(len(hsl)):
        if hsl[i] == "h":
            if hsl[i+3] != "(":
                return False
    h, s, l = hsl.split(",")
    h = h.replace("hsl(", "").strip()
    if not h.isdigit():
        return False
    s = s.strip()
    if not s.endswith("%"):
        return False
    s = s[:-1]
    if not s.isdigit():
        return False
    l = l.strip()
    temp = ""
    for i in l:
        if i.isdigit():
            temp += i
        else:
            if i == "%":
                break
            else:
                return False
    l = temp 
    return (0 <= int(h) <= 360) and (0 <= int(s) <= 100) and (0 <= int(l) <= 100)


""" def is_valid_hsl(hsl):
    # Remove trailing semicolon and spaces
    hsl = hsl.strip().rstrip(";").strip()

    # Must start with 'hsl(' and end with ')'
    if not hsl.startswith("hsl(") or not hsl.endswith(")"):
        return False

    # Extract the values inside parentheses
    values = hsl[4:-1].split(",")

    if len(values) != 3:
        return False

    h, s, l = [v.strip() for v in values]

    # Validate hue
    if not h.isdigit():
        return False
    h = int(h)
    if not (0 <= h <= 360):
        return False

    # Validate saturation and lightness
    for value in (s, l):
        if not value.endswith("%"):
            return False
        number = value[:-1].strip()
        if not number.isdigit():
            return False
        number = int(number)
        if not (0 <= number <= 100):
            return False

    return True """
