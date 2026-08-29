from math import gcd

def get_odds(dice, target):
    dp = [[0] * (target + 1) for _ in range(dice + 1)]
    dp[0][0] = 1

    # builds the probability table
    for i in range(1, dice + 1):
        for t in range(1, target + 1):
            for face in range(1, 7):
                if t - face >= 0:
                    dp[i][t] += dp[i - 1][t - face]

    ways = dp[dice][target]
    total = 6 ** dice
    common = gcd(ways, total)

    return f"{ways // common} in {total // common}"
