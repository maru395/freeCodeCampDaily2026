def mirror(s):
    # ::-1 is used for slicing start:stop:step
    reverse = s[::-1]
    return  f"{s}{reverse}"
