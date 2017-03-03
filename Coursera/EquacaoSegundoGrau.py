a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

math.sqrt(2)

delta = (b**2) - 4 * a * c

if delta > 0:

    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
else:
    print ('O valor de Delta é ', delta ,' Pertencendo portanto aos números Imaginarios, boa sorte :D')
