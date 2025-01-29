import math

print("Calculadora de Bháskara")

a = float(input("Informe o coeficiente a: "))
b = float(input("Informe o coeficiente b: "))
c = float(input("Informe o coeficiente c: "))

print(f"(a)x²+(b)x+(c)")

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raízes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Existe apenas uma raiz real: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Existem duas raízes reais: {raiz1} e {raiz2}")