def can_donate(donor, recipient):
    donor_letter = donor[:-1]
    donor_rh = donor[-1]
    
    recipient_letter = recipient[:-1]
    recipient_rh = recipient[-1]
    
    BLOOD_RULES = {
    "O":  {"O", "A", "B", "AB"},
    "A":  {"A", "AB"},
    "B":  {"B", "AB"},
    "AB": {"AB"}
    }
    RH_RULES = {
        "-": {"-", "+"},
        "+": {"+"}
    }
    
    return recipient_letter in BLOOD_RULES.get(donor_letter, set()) and recipient_rh in RH_RULES.get(donor_rh, set())
