def exact_change(amount):
    # Store the values of the available coins.
    coins = [1, 5, 10, 25]

    # Create a list from 0 to amount, initialized with zero ways.
    ways = [0] * (amount + 1)

    # Set one way to make 0 cents: use no coins.
    ways[0] = 1

    # Select each coin type one at a time.
    for coin in coins:

        # Visit every amount that can use the selected coin.
        for current_amount in range(coin, amount + 1):

            # Add all existing combinations for the remaining amount
            # to the number of combinations for the current amount.
            ways[current_amount] += ways[current_amount - coin]

    # Return the number of ways to make the requested amount.
    return ways[amount]
