def is_valid_schema(obj):
    vals = list(obj.values())
    
    if len(vals) < 3:
        return False
        
    return (isinstance(vals[0], str) and 
            isinstance(vals[1], int) and 
            isinstance(vals[2], bool))
