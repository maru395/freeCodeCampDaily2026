def do_math(s):
    parts = []
    i = 0

    # --- PASS 1: TOKENIZE ---
    # Scan the string once, grouping consecutive digits and non-digits separately
    while i < len(s):
        if s[i].isdigit():
            j = i
            # Extend j until we hit a non-digit (captures multi-digit numbers like "10")
            while j < len(s) and s[j].isdigit():
                j += 1
            parts.append(('num', int(s[i:j])))  # Store the integer value
            i = j
        else:
            j = i
            # Extend j until we hit a digit (captures letter groups like "ab")
            while j < len(s) and not s[j].isdigit():
                j += 1
            parts.append(('chars', j - i))  # Store only the LENGTH of the letter group
            i = j

    # --- PASS 2: EVALUATE ---
    # Walk tokens; when a number is found, check the token before it
    result = 0
    for i, part in enumerate(parts):
        if part[0] == 'num':
            if i == 0:
                result = part[1]  # First number becomes the starting value
            else:
                gap = parts[i - 1]  # The token immediately before this number
                if gap[0] == 'chars':
                    if gap[1] % 2 == 0:
                        result += part[1]  # Even letter count → addition  (e.g. "ab" = 2)
                    elif gap[1] % 2 != 0:
                        result -= part[1]  # Odd letter count  → subtraction (e.g. "a"  = 1)
    return result
