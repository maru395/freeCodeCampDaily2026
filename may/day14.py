def is_mirror_image(s1, s2):
    symmetric = set("WTYUIOHAXVMwoxv08=+:|-_*^!. ")
    mirror_pairs = {
        '[': ']', ']': '[',
        '{': '}', '}': '{',
        '<': '>', '>': '<',
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        '(': ')', ')': '(',
    }
    
    # Build the mirror of s1
    mirrored = []
    for ch in reversed(s1):
        if ch in symmetric:
            mirrored.append(ch)
        elif ch in mirror_pairs:
            mirrored.append(mirror_pairs[ch])
        else:
            return False  # character has no mirror equivalent
    
    return ''.join(mirrored) == s2
