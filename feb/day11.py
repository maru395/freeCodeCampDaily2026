def compute_score(judge_scores, *penalties):
    penalties = sum(i for i in penalties)
    max_score = max(judge_scores)
    min_score = min(judge_scores)
    sum_score = sum(judge_scores)
    return sum_score - max_score - min_score - penalties
    # one liner
    # return sum(judge_scores) - max(judge_scores) - min(judge_scores) - sum(i for i in penalties)
