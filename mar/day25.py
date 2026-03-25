from datetime import datetime, timedelta

def can_retake(finish_time, current_time):
    dt1 = datetime.fromisoformat(finish_time)
    dt2 = datetime.fromisoformat(current_time)
    return dt2 - dt1 >= timedelta(hours=48)
