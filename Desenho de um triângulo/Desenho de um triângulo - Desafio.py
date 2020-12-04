h = int(input("Digite a Altura: "))
com = int(input("Digite o Comprimento: "))


for l in range (1, h):
    for c in range(1, com, l):
        print(f"X", end="")
    print()