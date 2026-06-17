def cast(spells):
    spell_data = {
        "f": {"spell": "Fire", "category": "Destruction", "base_score": 3},
        "l": {"spell": "Lightning", "category": "Destruction", "base_score": 3},
        "i": {"spell": "Ice", "category": "Control", "base_score": 2},
        "w": {"spell": "Wind", "category": "Control", "base_score": 2},
        "h": {"spell": "Heal", "category": "Restoration", "base_score": 1},
        "s": {"spell": "Shield", "category": "Restoration", "base_score": 1}
    }
    score = 0
    prev = spell_data[spells[0]]["category"]

    for spell in spells:

        if spell_data[spell]["category"] != prev:
            prev = spell_data[spell]["category"]
            multiplier += 1
        else:
            multiplier = 1

        score += spell_data[spell]["base_score"] * multiplier

    return score

print(cast("fihwl"))
