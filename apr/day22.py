def get_cleanup_score(items):
    BASE_VALUES = {
        "bottle": 10, "can": 6, "bag": 8, "tire": 35,
        "straw": 4, "cardboard": 3, "newspaper": 3,
        "shoe": 12, "electronics": 25, "battery": 18, "mattress": 38
    }

    total      = 0
    prev_item  = None
    streak     = 0  # How many times the same item has appeared consecutively

    for i, item in enumerate(items):
        position = i + 1  # 1-based for fifth-item multiplier logic

        # --- Rare item: fixed value, no streak bonus ---
        if isinstance(item, list) and item[0] == "rare":
            score = item[1]
            prev_item = None  # Rare items break the streak
            streak = 0

        # --- Normal item ---
        else:
            base = BASE_VALUES[item]

            # Streak: same item as previous → increment streak, else reset to 0
            if item == prev_item:
                streak += 1
            else:
                streak = 0

            # Score = base + streak bonus (0 on first, +1 on second consecutive, etc.)
            score = base + streak
            prev_item = item

        # --- Fifth item multiplier: every 5th item gets *2, *3, *4... ---
        if position % 5 == 0:
            multiplier = (position // 5) + 1  # 5th=*2, 10th=*3, 15th=*4
            score *= multiplier

        total += score

    return total
