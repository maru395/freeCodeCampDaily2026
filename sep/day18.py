def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    gallons_needed = max(0, tank_size - fuel_level)
    cost = gallons_needed * price_per_gallon
    return f"${cost:.2f}"
