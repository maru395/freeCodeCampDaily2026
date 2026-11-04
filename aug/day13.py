def fibonacci_sequence(start_sequence, length):
    # Copy the starting values so the caller's list isn't modified.
    sequence = list(start_sequence)

    # Each new term is the sum of the last two terms, whatever they started as.
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])

    # Slice in case `length` is smaller than the starting list.
    return sequence[:length]
