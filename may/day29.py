import math

def get_wider_aspect_ratio(a, b):

    # helper function
    def get_aspect_ratio(s):
        w, h = s.split("x")
        d = math.gcd(int(w), int(h))

        rw = int(w) // d
        rh = int(h) // d
        return f"{rw}:{rh}"

    def compare_ratios(a, b):
        size_a = a.split("x")
        size_b = b.split("x")
        ratio_a = int(size_a[0]) / int(size_a[1])
        ratio_b = int(size_b[0]) / int(size_b[1])
        
        return a if ratio_a > ratio_b else b
        
    return get_aspect_ratio(compare_ratios(a, b))
