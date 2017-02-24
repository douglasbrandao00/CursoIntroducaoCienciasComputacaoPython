def fatorial (n):
    f = 1
    while (n > 1):
        f = f * n
        n = n -1
    return f

def numeroBinomial (n, k):
    return fatorial(n) / (fatorial(k) * fatorial (n - k))
