def compare_energy(calories_burned, watt_hours_used):
    cal = 4184 
    watt = 3600 
    if calories_burned*cal > watt*watt_hours_used:
        return "workout"
    elif calories_burned*cal < watt*watt_hours_used:
        return "devices"
    elif calories_burned*cal == watt*watt_hours_used:
        return "equal"
    else:
        return "error"
