def image_search(images, term):

    return list(c for c in images if term.lower() in c.lower())
