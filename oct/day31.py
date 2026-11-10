def spookify(boo):
    capitalize = True
    new_string = ""
    for i in range(len(boo)):
        if boo[i] == "_" or boo[i] == "-":
            new_string += "~"
        else:
            if capitalize:
                new_string += boo[i].upper()
                capitalize = False
            else:
                new_string += boo[i].lower()
                capitalize = True
    return new_string
