import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
}

def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        op = operators[(i - 1) % len(operators)] # loops thru the operators
        result = OPS[op](result, numbers[i]) # eval the last result to the current i
    return result
