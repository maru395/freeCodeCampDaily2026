compliments = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C",
}

def complementary_dna(strand):

    return "".join(compliments[c] for c in strand)
