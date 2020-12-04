matriz = [['Nº:', 'Soma:', 'Média:']]

soma = 0
media = 0
contador = 0
for i in range(0, 5):
    lista = []
    x = int(input('Acrescente um número para a Matriz: '))
    lista.append(x)

    soma += x
    lista.append(soma)

    contador += 1
    media = soma / contador
    lista.append(media)
    matriz.append(lista)


for parte in matriz:
    for item in parte:
        print(f'{item}  ', end='')
    print()
