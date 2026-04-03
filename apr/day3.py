def get_browser_history(commands):
    counter = -1
    history = []
    for i in commands:
        if i == "Back":
            if counter > 0:        
                counter -= 1
        elif i == "Forward":
            if counter < len(history) - 1:
                counter += 1 
        else:
            history = history[:counter + 1]
            counter += 1
            history.append(i)
    return [history, counter]

print(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]))
