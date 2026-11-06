import re

def rgb_to_hex(rgb):
    nums = re.findall(r"\d+", rgb)
    r, g, b = map(int, nums)
    return f"#{r:02x}{g:02x}{b:02x}"

# f"{n:d}"        # '255'          decimal
# f"{n:x}"        # 'ff'           hex, lowercase
# f"{n:X}"        # 'FF'           hex, uppercase
# f"{n:b}"        # '11111111'     binary
# f"{n:o}"        # '377'          octal
# f"{65:c}"       # 'A'            character from a code
# f"{3.14159:f}"  # '3.141590'     float (6 decimals by default)
# f"{1234.5:e}"   # '1.234500e+03' scientific notation
# f"{0.25:%}"     # '25.000000%'   percentage
