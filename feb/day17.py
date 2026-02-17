# adjust logic put total weight and len on top of if for faster call

def check_eligibility(athlete_weights, sled_weight):
    if (len(athlete_weights) == 1 and sled_weight >= 162 and (sum(athlete_weights) + sled_weight) < 247) or (len(athlete_weights) == 2 and sled_weight >= 170 and (sum(athlete_weights) + sled_weight) < 390) or (len(athlete_weights) == 4 and sled_weight >= 210 and (sum(athlete_weights) + sled_weight) <= 630):
        return "Eligible"
    else:        
        return "Not Eligible"
