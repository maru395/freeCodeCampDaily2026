def get_streaming_bill(cart, subscription):
    prices = {
        "HD": {"rent": 3.99, "buy": 12.99},
        "4K": {"rent": 5.99, "buy": 19.99},
    }
    discounts = {"none": 1.0, "basic": 0.9, "premium": 0.75}

    subtotal = 0
    for item in cart:
        fmt = item["format"]
        typ = item["type"]
        subtotal += prices[fmt][typ]
    subtotal = round(subtotal, 2)

    total = round(subtotal * discounts[subscription], 2)
    return f"${total:.2f}"
