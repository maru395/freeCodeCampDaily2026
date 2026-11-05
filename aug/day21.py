from datetime import timedelta  

def mile_pace(miles, duration):
    h, m = map(int, duration.split(":"))
    td = timedelta(hours=h, minutes=m) / miles   # timedelta supports / and //

    total_minutes = int(td.total_seconds() // 60)
    return f"{total_minutes // 60:02d}:{total_minutes % 60:02d}"
