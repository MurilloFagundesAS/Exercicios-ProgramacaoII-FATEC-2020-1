matriz = []
for i in range(0, 5):
    x = int(input('Digite um número para a matriz: '))
    matriz.append(x)
print(f'A matriz foi {matriz} !!!')

soma = 0
contador = 0
for i in range(0, len(matriz)):
    soma += matriz[i]
    contador += 1
media = soma / contador
print(f'A média da matriz foi {media}!!!')

matriz.sort()  # Ordena a matriz

if len(matriz) % 2 == 0:
    meio1 = len(matriz)/2 + 1
    meio2 = len(matriz)/2 - 1
    meio = meio1+meio2/2
else:
    meio = len(matriz)//2 + 1
