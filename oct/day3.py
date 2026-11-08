def check_strength(password):
    specials = "!@#$%^&*"
    rules = [
        len(password) >= 8,
        any(c.islower() for c in password) and any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in specials for c in password),
    ]

    score = sum(rules)

    if score == 4:
        return "strong"
    if score >= 2:
        return "medium"
    return "weak"
  
