def verify(message, key, signature):
    mine = yours = 0
    for c in message:
        if not c.isalpha():
            continue
        if c.isupper():
            mine += ord(c) - 38
        else:
            mine += ord(c) - 96
    for c in key:
        if not c.isalpha():
            continue
        if c.isupper():
            yours += ord(c) - 38
        else:
            yours += ord(c) - 96
    return mine +yours == signature
