# simple implementation using if else
def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    parameters = [distance_points, style_points, wind_comp, k_point_bonus] 
    point = sum(parameters)
    if point > 180:
        return "gold"
    elif point > 175 and point < 180:
        return "silver"
    elif point > 172 and point < 175:
        return "bronze"
    elif point == 172 or point == 175 or point == 180:
        return "tie"
    else:
        return "no medal"
