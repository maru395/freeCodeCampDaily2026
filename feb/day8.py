def calculate_penalty_distance(rounds):
    return sum((5 - i) * 150 for i in rounds)
