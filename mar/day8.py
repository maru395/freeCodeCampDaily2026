def get_element_size(window_size, element_vw, element_vh):
    return f"{int(window_size.split(' x ')[0]) * int((int(element_vw[:-2]) / 100))} x {int(window_size.split(' x ')[1]) * int((int(element_vh[:-2]) / 100))}"
