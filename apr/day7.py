import math

def palindrome_locator(s):
    if s == s[::-1]:
        if len(s) % 2 != 0:
            return s[int(len(s)/2)]
        else:
            return f"{s[math.ceil(len(s)/2)]}{s[math.floor(len(s)/2)]}"
    return "none"
