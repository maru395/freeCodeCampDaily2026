def is_valid_schema(obj):
    vals = list(obj.values())
    
    if len(vals) < 4:
        return False
        
    if (isinstance(vals[0], str) and isinstance(vals[1], int) and isinstance(vals[2], bool)):
        if vals[3] in ("user", "creator", "moderator", "staff", "admin"):
            return True
    return False
