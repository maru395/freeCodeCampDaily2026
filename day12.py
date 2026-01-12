def get_number_of_plants(field_size, unit, crop):
    if unit == "acres":
        x = 4046.68
    elif unit == "hectares":
        x = 10000
    else:
        return "invalid input"
    if crop == "corn":
        y = 1
    elif crop == "wheat":
        y = 0.1
    elif crop == "soybeans":
        y = 0.5
    elif crop == "tomatoes":
        y = 0.25
    elif crop == "lettuce":
        y = 0.2
    else:
        return "invalid input"
    return (int) (field_size*x/y)
