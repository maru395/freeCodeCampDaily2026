import math

def get_max_profit(prices, budget):
    n = len(prices)
    best_profit = 0

    for buy in range(n):
        shares = budget // prices[buy]  # whole shares only
        if shares <= 0:
            continue
        for sell in range(buy + 1, n):
            profit = shares * (prices[sell] - prices[buy])
            if profit > best_profit:
                best_profit = profit

    # round DOWN to the nearest cent
    rounded = math.floor(best_profit * 100 + 1e-9) / 100
    return f"{rounded:.2f}"
