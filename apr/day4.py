# add safeguards to eval

def is_valid_equation(equation):
    expression, val = equation.split(" = ")
    return True if eval(expression) == int(val) else False
