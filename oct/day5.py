def has_exoplanet(readings):
    levels = [int(c, 36) for c in readings]
    return 5 * min(levels) * len(levels) <= 4 * sum(levels)
