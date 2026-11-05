def decode(message, shift):
    decoded = ""
    for c in message:
        if not c.isalpha():
            # Leave spaces, punctuation, and digits unchanged
            decoded += c
        else:
            # chr() needs an ASCII code, and uppercase and lowercase letters start
            # at different codes (A = 65, a = 97), so pick the right starting point
            base = ord("A") if c.isupper() else ord("a")

            # ord(c) - base  -> convert the letter to a position from 0 to 25
            # - shift        -> undo the encoding (a negative shift goes the other way)
            # % 26           -> wrap around the alphabet, so going before A loops to Z
            # + base         -> convert the position back to an ASCII code,
            #                   keeping the original case
            decoded += chr((ord(c) - base - shift) % 26 + base)
    return decoded
