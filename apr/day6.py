from datetime import datetime

def get_day_of_week(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000).strftime("%A")
