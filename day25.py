def scale_image(size, scale):
    list_size = size.split("x")
    list_size = [int(s) for s in list_size]
    for i in range(len(list_size)):
        list_size[i] = int(list_size[i]*scale)
    return f"{list_size[0]}x{list_size[1]}"

# cleaner
# def scale_image(size, scale):
#     w, h = size.split("x")
#     w, h = int(float(w) * scale), int(float(h) * scale)
#     return f"{w}x{h}"
