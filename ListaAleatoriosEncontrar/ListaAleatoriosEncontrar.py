from random import randint

lista = []

for i in range(0,100):
    aleatorio = randint(1,100)
    lista.append(aleatorio)
print(lista)

numeroEncontrar = int(input('Deseja encontrar qual número? '))

if numeroEncontrar in lista:
    print(f'\33[31m{numeroEncontrar}\33[m está na lista!')
else:
    print(f'Não tem \33[31m{numeroEncontrar}\33[m nessa lista...')