def get_oldest(people):
    age = max(p['age'] for p in people)
    return [p['name'] for p in people if p['age'] == age]
# still slow tho
