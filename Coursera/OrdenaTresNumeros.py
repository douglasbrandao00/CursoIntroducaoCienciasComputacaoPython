a = int(input('Digite o primeiro: '))
b = int(input('Digite o segundo: '))
c = int(input('Digite o terceiro: '))

PrimeiroTeste = a > b
SegundoTeste  = b > c

print('')
print(PrimeiroTeste)
print(SegundoTeste)

if PrimeiroTeste and SegundoTeste:
    print(c, b, a)
