def get_initials(name):
    return "".join(word[0] + "." for word in name.split())
