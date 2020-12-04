matriz = []
for i in range(0, 5):
    x = int(input('Digite um número para a matriz: '))
    matriz.append(x)

print(f'A matriz foi {matriz} !!!')
print(f'O maior número dela é {max(matriz)}!!!')
print(f'O menor número dela é {min(matriz)}!!!')