from datetime import date
import calendar

def get_due_date(date_str):
    year, month, day = map(int, date_str.split("-"))
    
    new_month = (month - 1 + 9) % 12 + 1
    new_year = year + (month - 1 + 9) // 12
    
    last_day = calendar.monthrange(new_year, new_month)[1]
    new_day = min(day, last_day)
    return f"{new_year}-{new_month:02d}-{new_day:02d}"
