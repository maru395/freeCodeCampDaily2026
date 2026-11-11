from datetime import datetime

def get_weekday(date_string):
    d = datetime.strptime(date_string, "%Y-%m-%d")
    return d.strftime("%A") 
