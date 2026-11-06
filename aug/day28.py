def get_laptop_cost(laptops, budget):
    prices = sorted(set(laptops), reverse=True)   # unique, highest first

    if len(prices) >= 2 and prices[1] <= budget:
        return prices[1]

    affordable = [p for p in prices if p <= budget]
    return affordable[0] if affordable else 0
