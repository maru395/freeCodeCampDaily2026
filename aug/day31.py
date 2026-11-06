import random

colors = {
    "red":   "FF0000",
    "green": "00FF00",
    "blue":  "0000FF"
}

def generate_hex(color):
    if color not in colors:
        return "Invalid color"

    shade = f"{random.randint(0, 255):02X}"   # random 00-FF
    return colors[color].replace("FF", shade)
