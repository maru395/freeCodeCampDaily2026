def burn_candles(candles, leftovers_needed):
    total = leftover = candles

    while leftover >= leftovers_needed:
        made = leftover // leftovers_needed        # new candles from leftovers
        remainder = leftover % leftovers_needed    # leftovers that didn't get used
        total += made                              # we burn the new candles too
        leftover = remainder + made                # burned candles leave new leftovers

    return total
