from random import randint

player = int(input('Chute um número entre 6 e 36: '))

d1 = randint(1, 6)
d2 = randint(1, 6)
d3 = randint(1, 6)
d4 = randint(1, 6)
d5 = randint(1, 6)
d6 = randint(1, 6)

soma = d1 + d2 + d3 + d4 + d5 + d6

while player <=36 and player > 0:
    pc = randint(1, 36)

    if soma == player:
        print('O Jogador Ganhou!!!')
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player =+ 100
        player = int(input('Chute outro número entre 6 e 36: '))
    elif soma == pc:
        print('O PC Ganhou!!!')
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player =+ 100
    elif player <= soma+5 and player >= soma-5:
        print("O Jogador Está Mais Perto, Diferença de 5!!!")
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player = int(input('Chute outro número entre 6 e 36: '))
    elif pc <= soma+5 and pc >= soma-5:
        print("O PC Está Mais Perto, Diferença de 5!!!")
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player = int(input('Chute outro número entre 6 e 36: '))
    elif player <= soma+10 and player >= soma-10:
        print("O Jogador Está Mais Perto, Diferença de 10!!!")
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player = int(input('Chute outro número entre 6 e 36: '))
    elif pc <= soma+10 and pc >= soma-10:
        print("O PC Chegou Está Mais Perto, Diferença de 10!!!")
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player = int(input('Chute outro número entre 6 e 36: '))
    elif player <= soma+20 and player >= soma-20:
        print("O Jogador Está Está Mais Perto, Diferença de 20!!!")
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player = int(input('Chute outro número entre 6 e 36: '))
    elif pc <= soma+20 and pc >= soma-20:
        print("O PC Chegou Está Mais Perto, Diferença de 20!!!")
        print(f'\nplayer  = {player}, pc = {pc} e a soma = {soma}\n')
        player = int(input('Chute outro número entre 6 e 36: '))
    else:
        print('Deu Ruim!!!')

print('Fim de Jogo!!!')