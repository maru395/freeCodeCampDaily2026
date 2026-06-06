def is_valid_schema(obj):
    # 1. Guard clause: Ensure optional 'supporter' is explicitly a boolean if present
    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False

    # 2. Strict type checks for required keys
    #    We must add 'and not isinstance(..., bool)' to 'posts' to block True/False
    is_valid_types = (
        isinstance(obj.get("username"), str) and
        isinstance(obj.get("posts"), int) and not isinstance(obj["posts"], bool) and
        isinstance(obj.get("verified"), bool)
    )

    # 3. Check roles only if the structural types match
    if is_valid_types:
        if obj.get("role") in ("user", "creator", "moderator", "staff", "admin"):
            return True

    return False

# This will now correctly return False
print(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}))
