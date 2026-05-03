from datetime import datetime, time

def get_greeting(s):
    given_time = datetime.strptime(s, "%H:%M").time()
    if time(5,0) <= given_time < time(12,0):
        greeting = "Good morning"
    elif time(12,0) <= given_time < time(18,0):
        greeting = "Good afternoon"
    elif time(18,0) <= given_time < time(22,0):
        greeting = "Good evening"
    else:
        greeting = "Good night"
    return greeting
