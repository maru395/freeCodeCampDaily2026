def battle(my_army, opposing_army):
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"
    else:
        blue = red = 0
        for i in range(len(my_army)):
            blue_val = red_val = 0

            # blue check
            if my_army[i].isalpha():
                if(my_army[i].islower()):
                    blue_val = ord(my_army[i]) - 96
                else:
                    blue_val = ord(my_army[i]) - 38
            elif my_army[i].isdigit():
                blue_val = int(my_army[i])
            
            # red check
            if opposing_army[i].isalpha():
                if(opposing_army[i].islower()):
                    red_val = ord(opposing_army[i]) - 96
                else:
                    red_val = ord(opposing_army[i]) - 38
            elif opposing_army[i].isdigit():
                red_val = int(opposing_army[i])
            
            if blue_val > red_val:
                blue += 1
            elif blue_val < red_val:
                red += 1
            blue += 1
            red += 1
        if blue > red:
            return "We won"
        elif blue < red:
            return "We lost"
        return "It was a tie"

print(battle("Hello", "World"))
