import re
def to_camel_case(s):
    words = re.split(r"[ \-_]", s)
    camel = words[0].lower()
    for w in range(1, len(words)):
        camel += words[w].title()
    return camel
