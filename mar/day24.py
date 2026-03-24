def passing_count(scores, passing_score):
    return sum(1 for x in scores if x >= passing_score)
