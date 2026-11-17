def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False

    differences = 0

    for a, b in zip(fingerprint_a, fingerprint_b):
        if a != b:
            differences += 1

    return differences <= len(fingerprint_a) * 0.10
