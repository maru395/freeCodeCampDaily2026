def get_contrast_rating(rgb1, rgb2, is_large_text):
    def get_luminance(rgb):
        channels = []
        for val in rgb:
            c = val / 255.0
            
            if c <= 0.04045:
                c = c / 12.92
            else:
                c = ((c + 0.055) / 1.055) ** 2.4
            
            channels.append(c)
            
        return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]

    l1 = get_luminance(rgb1)
    l2 = get_luminance(rgb2)

    lighter = max(l1, l2)
    darker = min(l1, l2)
    contrast = (lighter + 0.05) / (darker + 0.05)

    if not is_large_text:
        if contrast >= 7.0:
            return "AAA"
        elif contrast >= 4.5:
            return "AA"
        else:
            return "Fail"
    else:
        if contrast >= 4.5:
            return "AAA"
        elif contrast >= 3.0:
            return "AA"
        else:
            return "Fail"
