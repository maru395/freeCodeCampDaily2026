def count(text, parameter):
    return sum(text.startswith(parameter, i) for i in range(len(text)))
