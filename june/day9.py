def get_roommates(people):
    gs = {}
    arr = []
    
    # Group people by their group ID/name
    for group in people:
        gs.setdefault(group["group"], []).append(group["name"])
    
    # Process each group and split them into pairs of max 2
    for g in gs.values():
        for i in range(0, len(g), 2):
            # Take a slice of up to 2 people
            room = g[i:i+2] 
            arr.append(" and ".join(room))
            
    return arr
