# salamat claude

def get_rotation(n):
    rot = 0
    num = n
    for x in range(len(str(abs(n)))):
        if num % len(str(abs(n))) == 0:
            return rot
        temp = str(num)[0]
        num = int(str(num)[1:] + temp)
        rot += 1
    return "none"

print(get_rotation(123))
