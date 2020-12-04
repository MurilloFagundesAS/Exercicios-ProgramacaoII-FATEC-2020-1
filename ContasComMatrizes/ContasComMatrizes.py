matrizA = []
matrizB = []
lista = []
matrizC = []


def adicao(matriz1, matriz2):
    global lista, matrizC
    matrizC = []
    for i in range(0, 2):
        for j in range(0,2):
            x = matriz1[i][j] + matriz2[i][j]
            lista.append(x)
        matrizC.append(lista)
        lista = []
    return matrizC


def subtracaoAB(matriz1, matriz2):
    global lista, matrizC
    matrizC = []
    for i in range(0, 2):
        for j in range(0,2):
            x = matriz1[i][j] - matriz2[i][j]
            lista.append(x)
        matrizC.append(lista)
        lista = []
    return matrizC


def subtracaoBA(matriz1, matriz2):
    global lista, matrizC
    matrizC = []
    for i in range(0, 2):
        for j in range(0,2):
            x = matriz1[i][j] - matriz2[i][j]
            lista.append(x)
        matrizC.append(lista)
        lista = []
    return matrizC


def multiplicaAB(matriz1, matriz2):
    global lista, matrizC
    matrizC = []
    lista = []
    a = (matriz1[0][0] * matriz2[0][0]) + (matriz1[0][1] * matriz2[1][0])
    b = (matriz1[0][0] * matriz2[0][1]) + (matriz1[0][1] * matriz2[1][1])
    lista.append(a)
    lista.append(b)
    matrizC.append(lista)
    lista = []

    c = (matriz1[1][0] * matriz2[0][0]) + (matriz1[1][1] * matriz2[1][0])
    d = (matriz1[1][0] * matriz2[0][1]) + (matriz1[1][1] * matriz2[1][1])
    lista.append(c)
    lista.append(d)
    matrizC.append(lista)
    lista = []

    return matrizC


def multiplicaBA(matriz1, matriz2):
    global lista, matrizC
    matrizC =[]
    lista = []
    a = (matriz1[0][0] * matriz2[0][0]) + (matriz1[0][1] * matriz2[1][0])
    b = (matriz1[0][0] * matriz2[0][1]) + (matriz1[0][1] * matriz2[1][1])
    lista.append(a)
    lista.append(b)
    matrizC.append(lista)
    lista = []

    c = (matriz1[1][0] * matriz2[0][0]) + (matriz1[1][1] * matriz2[1][0])
    d = (matriz1[1][0] * matriz2[0][1]) + (matriz1[1][1] * matriz2[1][1])
    lista.append(c)
    lista.append(d)
    matrizC.append(lista)
    lista = []

    return matrizC


def identidade():
    matrizC = [[1, 0], [0, 1]]
    return matrizC


def inversa():
    print(f'Desculpa, só consegui fazer até aqui')


def resposta(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f'{elemento} ', end='')
        print()


# Matriz A
for i in range(0, 2):
    for j in range(0,2):
        x = int(input(f'Adiciona o elemento {i+1}x{j+1} da matriz A: '))
        lista.append(x)
    matrizA.append(lista)
    lista = []

# Matriz B
print()
for i in range(0, 2):
    for j in range(0,2):
        x = int(input(f'Adiciona o elemento {i+1}x{j+1} da matriz B: '))
        lista.append(x)
    matrizB.append(lista)
    lista = []


# Printa matriz A
for linha in matrizA:
    for elemento in linha:
        print(f'{elemento} ', end='')
    print()

# Printa matriz B
print()
for linha in matrizB:
    for elemento in linha:
        print(f'{elemento} ', end='')
    print()


# Menu de opções
while True:
    print('''
    Menu de Opções
1 = Adição de Matrizes
2 = Subtração de A por B
3 = Subtração de B por A
4 = Multiplicação de A por B
5 = Multiplicação de B por A
6 = Matriz identidade
    ''', end='')
    opcao = int(input('O que deseja fazer: '))
    print()

    if opcao == 1:
        # Adição
        adicao(matrizA, matrizB)
        print(f'A soma das matrizes deu: ')
        resposta(matrizC)

    elif opcao == 2:
        # Subtração A por B
        subtracaoAB(matrizA, matrizB)
        print(f'A subtração da matriz A pela matriz B deu: ')
        resposta(matrizC)

    elif opcao == 3:
        # Subtração B por A
        subtracaoBA(matrizB, matrizA)
        print(f'A subtração da matriz B pela matriz A deu: ')
        resposta(matrizC)

    elif opcao == 4:
        # Multiplicação A por B
        multiplicaAB(matrizA, matrizB)
        print(f'A multiplicação da matriz A pela matriz B deu: ')
        resposta(matrizC)

    elif opcao == 5:
        # Multiplicação B por A
        multiplicaBA(matrizB, matrizA)
        print()
        print(f'A multiplicação da matriz B pela matriz A deu: ')
        resposta(matrizC)

    elif opcao == 6:
        # Matriz identidade
        identidade()
        print()
        print(f'A matriz identidade é: ')
        resposta(matrizC)

    elif opcao == 7:
        # Matriz inversa
        inversa()
    else:
        print('Opção inválida! Tente novamente')
        continue

    sair = str(input('Deseja Sair: [S/N]')).strip().upper()[0]
    if sair == 'S':
        break
print('Programa Encerrado!')
