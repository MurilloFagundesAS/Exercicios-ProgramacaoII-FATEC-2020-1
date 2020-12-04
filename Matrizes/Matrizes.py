matriz = [[], [], [], []]

# Cria a matriz
for j in range(0, 4):
    for i in range(0, 4):
        x = int(input(f'Digite o elemento {j+1}x{i+1} da matriz: '))
        matriz[j].append(x)


# Printa a matriz
for listas in matriz:
    for item in listas:
        print(f'{item}  ', end='')
    print()
print()


# Soma linhas
soma = 0
for i in range(0, 4):
    for j in range(0, 4):
        soma += matriz[i][j]
    print(f'Soma da {i+1} ª linha: {soma}!!!')
    soma = 0
print()


# Soma Coluna
soma = 0
numero = 0
for k in range(0,4):
    for i in range(0,4):
        for j in range(0, 4):
            if j == numero:
                soma += matriz[i][numero]
    print(f'A soma da coluna {i+1}ª é {soma}!!!')
    numero+=1
    soma = 0
print()


# Diagonal principal
soma = 0
for i in range(0,4):
    for j in range(0, 4):
        if j == i:
            soma += matriz[i][j]
print(f'A soma da diagonal principal é {soma}!!!')
print()


# Soma da diagonal secundária
soma = 0
numero = 3
for i in range(0, 4):
    for j in range(0,4):
        if j == numero:
            soma += matriz[i][numero]
            numero -= 1
print(f'A soma da diagonal secundária é {soma}!!!')
