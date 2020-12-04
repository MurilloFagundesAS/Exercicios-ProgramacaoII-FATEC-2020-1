from random import randint

print('Digite:\n1 para jogar Pedra\n2 para jogar Papel\n3 para jogar Tesoura\nOu outro número para não jogar')
player = int(input())

while player <=3 and player >=1:
    pc = randint(1, 3)
    if pc == 1 and player == 2:
        print('O PC escolheu Pedra\nVocê escolheu Papel\nVocê ganhou!!!')
        player = int(input('Digite de 1 a 3 para Jogar de Novo!!! Ou um maaior que 3 para sair!! '))
    elif pc == 1 and player == 3:
        print('O PC escolheu Pedra\nVocê escolheu Tesoura!!!O PC ganhou!!!')
        player = int(input('Digite de 1 a 3 para Jogar de Novo!!! Ou um maaior que 3 para sair!! '))
    elif pc == 1 and player == 1:
        player = int(input('Empate!!!\nAmbos escolheram Pedra\nDigite de 1 a 3 para Jogar de Novo! '))
    elif pc == 2 and player == 1:
        print('O PC escolheu Papel\nVocê escolheu Pedra!!!\nO PC ganhou!!!')
        player = int(input('Digite de 1 a 3 para Jogar de Novo!!! Ou um maaior que 3 para sair!! '))
    elif pc == 2 and player == 3:
        print('O PC escolheu Papel\nVocê escolheu Tesoura!!!\nVocê ganhou!!!')
        player = int(input('Digite de 1 a 3 para Jogar de Novo!!! Ou um maaior que 3 para sair!! '))
    elif pc == 2 and player == 2:
        player = int(input('Empate!!!\nAmbos escolheram Papel\nDigite de 1 a 3 para Jogar de Novo! '))
    elif pc == 3 and player == 1:
        print('O PC escolheu Tesoura\nVocê escolheu Pedra\nVocê ganhou!!!')
        player = int(input('Digite de 1 a 3 para Jogar de Novo!!! Ou um maaior que 3 para sair!! '))
    elif pc == 3 and player == 2:
        print('O PC escolheu Tesoura\nVocê escolheu Papel\nO PC ganhou!!!')
        player = int(input('Digite de 1 a 3 para Jogar de Novo!!! Ou um maaior que 3 para sair!! '))
    elif pc == 3 and player == 3:
        player = int(input('Empate!!!\nAmbos escolheram Tesoura\nDigite de 1 a 3 para Jogar de Novo!'))
    else:
        player = int(input('Algo deu errado...\nTente de Novo!\nDigite um número de 1 a 3 para jogar'))
    print()
print('Você decidiu parar de jogar...Que Pena!!')