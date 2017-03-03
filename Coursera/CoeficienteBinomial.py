def fatorial(n):
    fatorial = 1
    while (n > 1):
        fatorial = fatorial * n
        n = n - 1
    return fatorial

def coeficienteBinomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))
