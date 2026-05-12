# c optimized way is data is static
def get_oldest(people):
    age = max(p['age'] for p in people)
    return [p['name'] for p in people if p['age'] == age]
# if dynamic
# def get_oldest(people):
#     if not people: return []
    
#     max_age = -1
#     oldest_names = []
    
#     for p in people:
#         age = p['age']
#         if age > max_age:
#             max_age = age
#             oldest_names = [p['name']] # Found a new leader, reset list
#         elif age == max_age:
#             oldest_names.append(p['name']) # It's a tie
            
#     return oldest_names
