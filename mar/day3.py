import math

def count_perfect_cubes(a, b):
    return sum((math.cbrt(i)).is_integer() for i in range(a, b + (-1 if a > b else 1), -1 if a > b else 1))
# for faster way we can use mathematical formula for checking the perfect cubes in a range: $$\text{Count} = \lfloor \sqrt[3]{\text{end}} \rfloor - \lceil \sqrt[3]{\text{start}} \rceil + 1$$
# count = max(0, math.floor(math.cbrt(b - 1)) - math.ceil(math.cbrt(a)) + 1)
