def format_coffee_order(order):
    menu = {
        "cold brew":4.50,
        "oat latte":5.00,
        "cappuccino":4.75,
        "espresso":3.00,
        "vanilla syrup":0.75,
        "caramel drizzle":0.60,
        "extra shot":0.50,
        "oat milk":0.75,
        "cream":0.75
    }
    included = ""
    total = 0
    for i in menu:
        if i in order:
            if included == "":
                included += i
                total += menu[i]
            else:
                total += menu[i]
                included += f" + {i}" 
    return f"{included}: ${total:.2f}"
