from collections import Counter

def triage_blood(bank, patients):
    compatible = Counter(bank)

    # Each type's accepted donors, most-preferred first
    PRIORITY = {
        "O":  ["O"],
        "A":  ["A", "O"],
        "B":  ["B", "O"],
        "AB": ["AB", "A", "B", "O"],  
    }

    served = 0
    for p in patients:
        for blood in PRIORITY[p]:
            if compatible[blood]:       # Counter returns 0 for missing keys
                compatible[blood] -= 1
                served += 1
                break

    return f"{served} of {len(patients)} patients served"
