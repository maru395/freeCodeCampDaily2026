from datetime import datetime

def to_12(time):

    return datetime.strptime(time, "%H%M").strftime("%I:%M %p").lstrip("0")
