a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número:"))
x: int

if a > b:
    x = a
    a = b
    b = x

print(f"{a} e {b}")