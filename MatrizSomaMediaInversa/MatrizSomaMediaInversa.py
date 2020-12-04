matriz = []

for i in range(0, 20):
    x = int(input('Acrescente um número para a Matriz: '))
    matriz.append(x)

matriz.reverse()

soma = 0
media = 0
contador = 0
invertido = []
for item in matriz:
    lista = []
    lista.append(item)

    soma += item
    lista.append(soma)

    contador+=1
    media = soma / contador
    lista.append(media)

    invertido.append(lista)

invertido.insert(0, ['Nº', 'Soma', 'Média'])

for listas in invertido:
    for item in listas:
        print(f'{item}  ', end='')
    print()

