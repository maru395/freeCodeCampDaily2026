def triage_issue(ms, message):
    if ms < 604800000:
        return "leave it"
    elif ms >= 604800000 and ("bump" in message or "Bump" in message):
        return "close it"
    else: 
        return "bump it"
    
