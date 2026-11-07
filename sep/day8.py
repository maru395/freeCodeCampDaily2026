ignore = {"a", "for", "an", "and", "by", "of"}

def build_acronym(s):
    return "".join(word[0].upper() for word in s.split(" ") if word not in ignore)
    
