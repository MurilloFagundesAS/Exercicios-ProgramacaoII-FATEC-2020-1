c = int(input("Qual O Comprimento Que Você Deseja?"))
h = int (input("Qual a Altura Que Você Deseja?"))

for i in range (1, h+1):
    for j in range (1, c+1):
        print(f"X", end="")
    print()