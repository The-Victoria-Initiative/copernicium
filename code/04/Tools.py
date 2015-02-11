def MinBases(n):
    i = 0
    while (True):
        if (2**i) >= n:
            return i
        i+=1

