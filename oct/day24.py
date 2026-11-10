def dive(ocean_map, coordinates):
    row, col = coordinates
    cell = ocean_map[row][col]

    if cell == "-":
        return "Empty"

    remaining = sum(r.count("O") for r in ocean_map)

    if cell == "O" and remaining == 1:
        return "Recovered"
    return "Found"
