import math

def get_pizzas_to_order(hours_worked):
    pizza = 8
    sum_person = 0
    for p in hours_worked:
        if math.ceil(p/3) >= 2:
            sum_person += math.ceil(p/3)
        else:
            sum_person += 2
        print(sum_person)
    return math.ceil(sum_person / pizza)

