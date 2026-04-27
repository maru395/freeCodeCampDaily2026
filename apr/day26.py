def explode_fizzbuzz(target):
    s = "fizzbuzz"
    steps = 0

    while s.count('z') < target:
        new_s = ""
        for i, ch in enumerate(s, 1):
            if i % 15 == 0:  new_s += "fizzbuzz"
            elif i % 3 == 0: new_s += "fizz"
            elif i % 5 == 0: new_s += "buzz"
            else:             new_s += ch
        s = new_s
        steps += 1

    return steps
