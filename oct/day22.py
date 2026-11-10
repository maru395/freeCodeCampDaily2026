words = {"have", "must", "are", "will", "can"}

def wise_speak(sentence):
    punct = sentence[-1] if sentence[-1] in ".!?" else ""
    end = []
    current = []
    switch = False

    for word in sentence.rstrip(".!?").split():
        if not switch:
            end.append(word)
        else:
            current.append(word)
        if word.lower() in words:
            switch = True

    first = " ".join(current)
    second = " ".join(end)
    first = first[0].upper() + first[1:]
    second = second[0].lower() + second[1:]
    return f"{first}, {second}{punct}"
