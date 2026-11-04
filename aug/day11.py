vowels = {"a", "e", "i", "o", "u"}

def is_balanced(s):
    half = len(s) // 2
    left = s[:half]
    right = s[half + len(s) % 2:]

    left_vowels = sum(char.lower() in vowels for char in left)
    right_vowels = sum(char.lower() in vowels for char in right)

    return left_vowels == right_vowels
