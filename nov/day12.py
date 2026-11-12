def generate_signature(name, title, company):
    first_letter = ord(name[0].lower()) - 97
    prefix  = ""
    if first_letter < 10:
        prefix  += ">>"
    elif first_letter < 19:
        prefix  += "--"
    else:
        prefix  += "::"
    return f"{prefix }{name}, {title} at {company}"
