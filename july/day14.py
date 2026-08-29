def pet_years(pet, age):
    multiplier = {
        "dog": 7,
        "cat": 6,
        "rabbit": 8,
        "hamster": 30,
        "guinea pig": 12,
        "goldfish": 6,
        "bird": 5
    }
    return age * multiplier[pet]
