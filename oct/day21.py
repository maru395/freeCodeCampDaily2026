def adjust_thermostat(current_f, target_c):
    target_f = target_c * 1.8 + 32
    diff = round(target_f - current_f, 1)

    if diff > 0:
        return f"Heat: {diff:.1f} degrees Fahrenheit"
    if diff < 0:
        return f"Cool: {abs(diff):.1f} degrees Fahrenheit"
    return "Hold"
