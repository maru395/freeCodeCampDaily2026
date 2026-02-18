import math

def calculate_start_delays(jump_scores):
    scores = []
    best_score = max(jump_scores)
    for j in jump_scores:
        scores.append(math.ceil((best_score - j) * 1.5))
    return scores
