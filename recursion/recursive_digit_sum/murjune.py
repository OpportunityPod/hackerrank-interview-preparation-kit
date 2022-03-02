def superDigit(n, k):
    if len(n) == 1: return n

    res = 0
    for i in n:
        res += int(i)
    res *= k
    return superDigit(str(res), 1)
