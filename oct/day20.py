def calculate_tips(meal_price, custom_tip):
    price = float(meal_price.lstrip("$"))
    tip = float(custom_tip.rstrip("%")) / 100
    return [f"${price * 0.15:.2f}", f"${price * 0.20:.2f}", f"${price * tip:.2f}"]
