def is_valid_schema(obj):
    # 1. Base validation: Ensure root input is a dictionary and contains 'users'
    if not isinstance(obj, dict) or "users" not in obj:
        return False
        
    users_list = obj.get("users")
    if not isinstance(users_list, list):
        return False

    # Allowed roles for inner check
    allowed_roles = ("user", "creator", "moderator", "staff", "admin")

    # 2. Iterate and validate each user profile inside the list
    for user in users_list:
        # Each profile must be a dictionary
        if not isinstance(user, dict):
            return False

        # Guard clause: Check optional 'supporter' field if it exists
        if "supporter" in user and not isinstance(user["supporter"], bool):
            return False

        # Strict structural type checks for required fields
        is_valid_types = (
            isinstance(user.get("username"), str) and
            isinstance(user.get("posts"), int) and not isinstance(user.get("posts"), bool) and
            isinstance(user.get("verified"), bool) and 
            isinstance(user.get("badges"), list)
        )
        if not is_valid_types:
            return False

        # Deep validation: Check list content and permitted role values
        all_badges_are_strings = all(isinstance(badge, str) for badge in user["badges"])
        valid_role = user.get("role") in allowed_roles

        if not (all_badges_are_strings and valid_role):
            return False

    # If all items in the array successfully pass validation
    return True
