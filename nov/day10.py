def get_extension(filename):
    if "." not in filename:
        return "none"
    ext = filename.rsplit(".", 1)[-1]
    return ext if ext else "none"
