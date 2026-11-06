def tribonacci_sequence(start_sequence, length):
    sequence = list(start_sequence)
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence[:length]
