def detect_mutations(strand1, strand2):
    
    indeces = []

    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            indeces.append(i)
    
    return indeces
