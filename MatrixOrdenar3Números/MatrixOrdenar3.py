lista = []

for i in range(0,3):
    x = int(input('Digite um número para a matriz: '))
    lista.append(x)

lista.sort()
print(f'Sua lista ordenada é {lista}')