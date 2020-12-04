from random import randint
from time import sleep
lista = []

print('{:=^35}'.format('Jogo dos Dados'))
playerDado = int(input('Em qual lado você vai apostar? '))
playerQtde = int(input('Quantas vezes você acha que\no lado \33[31m{}\33[m vai aparecer? '.format(playerDado)))
print('Você chutou que o \33[31mD{}\33[m irá aparecer \33[31m{}\33[m vezes!!!'.format(playerDado, playerQtde))

print('O \33[31mPC\33[m  está jogando...')
sleep(1)
pcDado = randint(1,6)
pcQtde = randint(1,6)
print('O PC chutou que o \33[31mD{}\33[m irá aparecer \33[31m{}\33[m vezes!!!'.format(pcDado, pcQtde))

print('Os \33[31mDADOS\33[m estão sendo jogados!!!')
for i in range(1,7):
    dado = randint(1,6)
    lista.insert(i, dado)
d1 = lista.count(1)
d2 = lista.count(2)
d3 = lista.count(3)
d4 = lista.count(4)
d5 = lista.count(5)
d6 = lista.count(6)
sleep(1)


if(d1>d2) and (d1>d3) and (d1>d4) and (d1>d5) and (d1>d6):
    print('O lado \33[31m1\33[m apareceu \33[31m{}\33[m vezes.\nEle é o que mais apareceu!!!'.format(d1))
    for j in range(1,7):
        if lista[j-1] == 1:
            print(f'\33[31m{lista[j-1]}\33[m ', end="")
        else:
            print(f'{lista[j-1]} ', end="")
    print()
    if playerDado == 1:
        if playerQtde == d1:
            print('VOCÊ \33[31mACERTOU\33[m!!!')
    elif pcDado == 1:
        if pcQtde == d1:
            print('O PC \33[31mACERTOU\33[m!!!')
    else:
        print('Ninguém acertou...')
elif(d2>d1) and (d2>d3) and (d2>d4) and (d2>d5) and (d2>d6):
    print('O lado \33[31m2\33[m apareceu \33[31m{}\33[m vezes.\nEle é o que mais apareceu!!!'.format(d2))
    for j in range(1,7):
        if lista[j-1] == 2:
            print(f'\33[31m{lista[j-1]}\33[m ', end="")
        else:
            print(f'{lista[j-1]} ', end="")
    print()
    if playerDado == 2:
        if playerQtde == d2:
            print('VOCÊ \33[31mACERTOU\33[m!!!')
    elif pcDado == 2:
        if pcQtde == d2:
            print('O PC \33[31mACERTOU\33[m!!!')
    else:
        print('Ninguém acertou...')
elif(d3>d1) and (d3>d2) and (d3>d4) and (d3>d5) and (d3>d6):
    print('O lado \33[31m3\33[m apareceu \33[31m{}\33[m vezes.\nEle é o que mais apareceu!!!'.format(d3))
    for j in range(1,7):
        if lista[j-1] == 3:
            print(f'\33[31m{lista[j-1]}\33[m ', end="")
        else:
            print(f'{lista[j-1]} ', end="")
    print()
    if playerDado == 3:
        if playerQtde == d3:
            print('VOCÊ \33[31mACERTOU\33[m!!!')
    elif pcDado == 3:
        if pcQtde == d3:
            print('O PC \33[31mACERTOU\33[m!!!')
    else:
        print('Ninguém acertou...')
elif(d4>d1) and (d4>d2) and (d4>d3) and (d4>d5) and (d4>d6):
    print('O lado \33[31m4\33[m apareceu \33[31m{}\33[m vezes.\nEle é o que mais apareceu!!!'.format(d4))
    for j in range(1,7):
        if lista[j-1] == 4:
            print(f'\33[31m{lista[j-1]}\33[m ', end="")
        else:
            print(f'{lista[j-1]} ', end="")
    print()
    if playerDado == 4:
        if playerQtde == d4:
            print('VOCÊ \33[31mACERTOU\33[m!!!')
    elif pcDado == 4:
        if pcQtde == d4:
            print('O PC \33[31mACERTOU\33[m!!!')
    else:
        print('Ninguém acertou...')
elif(d5>d1) and (d5>d2) and (d5>d3) and (d5>d4) and (d5>d6):
    print('O lado \33[31m5\33[m apareceu \33[31m{}\33[m vezes.\nEle é o que mais apareceu!!!'.format(d5))
    for j in range(1,7):
        if lista[j-1] == 5:
            print(f'\33[31m{lista[j-1]}\33[m ', end="")
        else:
            print(f'{lista[j-1]} ', end="")
    print()
    if playerDado == 5:
        if playerQtde == d5:
            print('VOCÊ \33[31mACERTOU\33[m!!!')
    elif pcDado == 5:
        if pcQtde == d5:
            print('O PC \33[31mACERTOU\33[m!!!')
    else:
        print('Ninguém acertou...')
elif(d6>d1) and (d6>d2) and (d6>d3) and (d6>d4) and (d6>d5):
    print('\nO lado \33[31m6\33[m apareceu \33[31m{}\33[m vezes.\nEle é o que mais apareceu!!!'.format(d6))
    for j in range(1,7):
        if lista[j-1] == 6:
            print(f'\33[31m{lista[j-1]}\33[m ', end="")
        else:
            print(f'{lista[j-1]} ', end="")
    print()
    if playerDado == 6:
        if playerQtde == d6:
            print('VOCÊ \33[31mACERTOU\33[m!!!')
    elif pcDado == 6:
        if pcQtde == d6:
            print('O PC\33[31mACERTOU\33[m!!!')
    else:
        print('Ninguém acertou...')
else:
    print(f'Nenhuma lado apareceu mais vezes...')
    print(f'{lista}')

print('{:=^35}'.format('FIM'),end='')