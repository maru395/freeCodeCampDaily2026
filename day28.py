# recursion to check each individual element
# extend make the list into a iliterable


def flatten(arr):
    flatten = []
    
    def one_dimensional(x):
        result = []
        for y in x:
            if isinstance(y, list):
                result.extend(one_dimensional(y))
            else:
                result.append(y)
        return result

    for x in arr:
        if isinstance(x, list):
            flatten.extend(one_dimensional(x))
        else:
            flatten.append(x)

    return flatten
