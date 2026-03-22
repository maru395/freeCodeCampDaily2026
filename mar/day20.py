def get_shadow(time):
    hour, mins = time.split(":")
    hour, mins = int(hour), int(mins)/60
    r = (abs((hour + mins)-12)) ** 3
    direction = ""
    if int(time.split(":")[0]) >= 18 or int(time.split(":")[0]) < 6 or int(time.split(":")[0]) == 12:
        return "No shadow"
    elif 12 < int(time.split(":")[0]):
        direction = "east"
    elif 12 > int(time.split(":")[0]):
        direction = "west"
    return f"{r:g}ft {direction}"
