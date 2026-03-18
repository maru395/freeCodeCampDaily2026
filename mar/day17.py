def get_milestone(years):
    return (
        "Newlyweds" if years < 1 else
        "Paper" if years < 5 else
        "Wood" if years < 10 else
        "Tin" if years < 25 else
        "Silver" if years < 40 else
        "Ruby" if years < 50 else
        "Gold" if years < 60 else
        "Diamond" if years < 70 else
        "Platinum"
    )
