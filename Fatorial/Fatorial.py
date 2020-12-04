x = int(input("Digite um número para saber seu fatorial:"))

fatorial = 1
for i in range(x, 0, -1):
    fatorial = fatorial * i

print(f"O fatorial de {x} é {fatorial}")