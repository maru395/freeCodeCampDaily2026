def i_before_e(sentence):
    result = list(sentence)
    for i in range(1, len(result)):
        after_c = result[i-2].lower() == "c" if i >= 2 else False

        if after_c:
            # after "c", "ie" is wrong → swap to "ei"
            if result[i-1].lower() == "i" and result[i].lower() == "e":
                result[i-1], result[i] = result[i], result[i-1]
        else:
            # without "c", "ei" is wrong → swap to "ie"
            if result[i-1].lower() == "e" and result[i].lower() == "i":
                result[i-1], result[i] = result[i], result[i-1]

    return "".join(result)
