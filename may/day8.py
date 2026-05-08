from datetime import datetime, timedelta

def medication_reminder(medications, current_time):
    schedules = {
        "Deployxitrin": ["08:00", "16:00"],
        "Debuggamanizole": ["07:00", "13:00", "21:00"],
        "Mergeflictamine": {"interval_hours": 4}
    }

    current = datetime.strptime(current_time, "%H:%M")
    soonest = None
    soonest_name = None

    for medicine, last_taken in medications:
        last = datetime.strptime(last_taken, "%H:%M")

        if medicine not in schedules:
            continue

        schedule = schedules[medicine]

        if isinstance(schedule, dict):
            interval = timedelta(hours=schedule["interval_hours"])
            next_dose = last + interval
            time_until = next_dose - current
        else:
            next_dose = None
            for time_str in schedule:
                dose_time = datetime.strptime(time_str, "%H:%M")
                if dose_time > current:
                    next_dose = dose_time
                    break
            if next_dose is None:
                continue
            time_until = next_dose - current

        if time_until.total_seconds() > 0:
            if soonest is None or time_until < soonest:
                soonest = time_until
                soonest_name = medicine

    if soonest is None:
        return "No upcoming doses."

    hours, remainder = divmod(int(soonest.total_seconds()), 3600)
    minutes = remainder // 60
    return f"{soonest_name} in {hours}h {minutes}m"
