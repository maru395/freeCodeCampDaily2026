def sum_letters(s):
    return sum(ord(l.upper())-64 for l in s if l.isalpha())
