def is_valid_trick(trick_name):
    first_word, second_word = trick_name.split(" ")
    valid_first = [
    "Misty", "Ghost", "Thunder", "Solar",
    "Sky", "Phantom", "Frozen", "Polar"
    ]

    valid_second = [
        "Twister", "Icequake", "Avalanche",
        "Vortex", "Snowstorm", "Frostbite",
        "Blizzard", "Shadow"
    ]
    
    return first_word in valid_first and second_word in valid_second
