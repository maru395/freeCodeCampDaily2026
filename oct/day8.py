import math

def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start_zone = 0.95 * math.sqrt(luminosity)
    end_zone = 1.37 * math.sqrt(luminosity)
    return [round(start_zone, 2), round(end_zone, 2)]
