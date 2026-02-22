def count_medals(winners):
    # listing the unique countries
    unique_val = set()
    for v in winners:
        for i in v:
            unique_val.add(i)
    countries = {}

    # initializing the values of each countries
    for uni in unique_val:
        countries.setdefault(uni, [0,0,0,0])

    # setting the values
    for i in range(len(winners)):
        for j in range(len(winners)):
            val = winners[i][j]
            
            if val in countries:
                countries[val][j] += 1
            countries[val][3] += 1
    
    # making the final return
    final_str = f"Country,Gold,Silver,Bronze,Total\n"
    for c, val in countries.items():
        final_str += f"{c}, {', '.join(map(str, val))}\n"
    return final_str
