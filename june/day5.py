def is_valid_schema(obj):
    # 1. Guard clause: Ensure optional 'supporter' is explicitly a boolean if present
    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False

    # 2. Strict type checks for required fields (including basic list check)
    is_valid_types = (
        isinstance(obj.get("username"), str) and
        isinstance(obj.get("posts"), int) and not isinstance(obj.get("posts"), bool) and
        isinstance(obj.get("verified"), bool) and 
        isinstance(obj.get("badges"), list)
    )

    # 3. Deep validation: Ensure every single item in the badges list is a string
    if is_valid_types:
        all_badges_are_strings = all(isinstance(badge, str) for badge in obj["badges"])
        
        # 4. Final role and list content check
        if all_badges_are_strings and obj.get("role") in ("user", "creator", "moderator", "staff", "admin"):
            return True

    return False
