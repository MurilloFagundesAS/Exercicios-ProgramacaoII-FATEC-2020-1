x = int(input("Digite um número positivo:"))

soma = 0

for i in range(1, x+1):
    soma = soma + i
    print(f"{i}")

print(f"A Soma Total foi: {soma}")