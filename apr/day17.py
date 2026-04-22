def decode(message):
    # Key derived from first letters of challenge titles at multiples of 25
    # A=0, B=1, ... Z=25 (zero-based so % 26 wrapping works correctly)
    KEY = "WMIDHNEMOI"

    result = []
    key_idx = 0  # Separate index that only advances for letters, not spaces

    for char in message:
        if char == ' ':
            # Spaces are passed through unchanged, key index does NOT advance
            result.append(' ')
        else:
            # Get the shift value: A=0, B=1, ... Z=25
            shift = ord(KEY[key_idx % len(KEY)]) - ord('A')

            # Shift the encoded letter backward, wrap around with % 26
            # e.g. enc=Y(24), key=W(22) → (24 - 22) % 26 = 2 = C
            decoded = (ord(char) - ord('A') - shift) % 26

            result.append(chr(decoded + ord('A')))
            key_idx += 1  # Only advance for letters

    return ''.join(result)
