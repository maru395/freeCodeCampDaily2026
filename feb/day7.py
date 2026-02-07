def get_landing_stance(start_stance, rotation):
    rotations = abs(rotation) // 180
    if rotations % 2 == 0:
        return start_stance  
    else:
        return "Goofy" if start_stance == "Regular" else "Regular"
