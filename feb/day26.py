def count_letters_and_numbers(s):
    l = sum(c.isalpha() for c in s)
    n = sum(c.isnumeric() for c in s)
    return f"The string has {l} {'letter' if l == 1 else 'letters'} and {n} {'number' if n == 1 else 'numbers'}."
    # logic
    # l = 0
    # n = 0
    # for letter in s:
    #     if letter.isalpha():
    #         l+=1
    #     elif letter.isnumeric():
    #         n+=1
    #     else:
    #         pass
    # if l > 1:
    #     l = str(l)
    #     l += " letters"
    # else:
    #     l = str(l)
    #     l += " letter"
    # if n > 1:
    #     n = str(n)
    #     n += " numbers"
    # else:
    #     n = str(n)
    #     n += " number"
    # return f"The string has {l} and {n}."
