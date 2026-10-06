def piggy_bank(coins):
    bank = {
        'pennies'	: 0.01,
        'nickels'	: 0.05,
        'dimes'	    : 0.10,
        'quarters'	: 0.25
    }

    sum = 0
    for k, v in coins.items():
        sum += bank[k] * v
    
    return f'${sum:.2f}'
