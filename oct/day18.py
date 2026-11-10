def sock_pairs(pairs, cycles):
    socks = pairs * 2

    for c in range(1, cycles + 1):
        if c % 2 == 0:
            socks = max(0, socks - 1)   
        if c % 3 == 0:
            socks += 1                  
        if c % 5 == 0:
            socks = max(0, socks - 1)   
        if c % 10 == 0:
            socks += 2                  

    return socks // 2
