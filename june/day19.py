from datetime import datetime, timedelta
import math

def get_rental_cost(rental_ts, return_ts, tier):
    pricing = {
        1: (4.99, 3.99),
        3: (3.99, 2.99),
        7: (2.99, 0.99),
    }
    base, late_fee = pricing[tier]

    checkout = datetime.fromisoformat(rental_ts.replace("Z", "+00:00"))
    returned = datetime.fromisoformat(return_ts.replace("Z", "+00:00"))

    # Due date is "tier" days after checkout's date, at 12:00 PM UTC
    due_date = checkout.date() + timedelta(days=tier)
    due = datetime(due_date.year, due_date.month, due_date.day, 12, 0, tzinfo=checkout.tzinfo)

    late_days = 0
    if returned > due:
        diff_seconds = (returned - due).total_seconds()
        late_days = math.ceil(diff_seconds / 86400)

    total = round(base + late_fee * late_days, 2)
    return f"${total:.2f}"
