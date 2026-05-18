def get_bingo_range(letter):
    bingo = {
        "B" : range(1,16),
        "I" : range(16,31),
        "N" : range(31,46),
        "G" : range(46,61),
        "O" : range(61,76),
    }

    return list(bingo[letter])

# can use dynamic calculation for better storage use but worse time complexity
