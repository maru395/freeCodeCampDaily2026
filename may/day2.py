def get_deepest_brackets(s):
    max_depth = 0
    current_depth = 0
    start = 0
    best_start = 0
    best_end = 0

    for i in range(len(s)):
        if s[i] in "[({":
            current_depth += 1
            start = i + 1
            if current_depth > max_depth:
                max_depth = current_depth
                best_start = start
        if s[i] in "})]":
            if current_depth == max_depth:
                best_end = i
            current_depth -= 1

    return s[best_start:best_end]
