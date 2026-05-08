# idk man frfr search how substrings work

def get_longest_substring(s):
    for length in range(len(s)-1, 0, -1): # Start with longest possible length
        seen = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            if sub in seen:
                return sub
            seen.add(sub)
    return None
