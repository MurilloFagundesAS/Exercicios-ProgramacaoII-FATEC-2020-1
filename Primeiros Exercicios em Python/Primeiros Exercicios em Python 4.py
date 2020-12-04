import math

delta : int
x1 : float
x2 : float

a = int(input("Digite o número de A:"))
b = int(input("Digite o número de B:"))
c = int(input("Digite o número de C:"))

delta = (b*b) - (4*a*c)
print(f"Delta = {delta}")

if delta > 0:
    raiz = math.sqrt(delta)

    x1 = (-b + raiz) / (2 * a)
    print(f"X1 = {x1}")

    x2 = (-b - raiz) / (2 * a)
    print(f"X2 = {x2}")

else:
    print(f"Delta não tem raiz")