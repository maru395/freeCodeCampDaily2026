def get_allergen_friendly_meals(meals, allergens):
    available = []
    
    for meal_data in meals:
        name = meal_data[0]
        ingredients = meal_data[1]
        
        is_safe = True
        for item in ingredients:
            if item in allergens:
                is_safe = False
                break 
        
        if is_safe:
            available.append(name)
            
    return available

    
