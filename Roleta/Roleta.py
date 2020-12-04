from random import randint
from time import sleep

print('Jogo da Roleta')

dinheiroJogador = 1000
dinheiroBanca = 5000
sair = 'S'
pagamento = 0
print(f'Você começa com R${dinheiroJogador:.2f} e a Banca com R${dinheiroBanca:.2f}')

while sair != 'N':
    aposta = float(input('Deseja apostar quanto? '))

    if aposta > dinheiroJogador:
        print('Você não tem esse dinheiro! Aposte outro valor!')
        continue
    else:
        dinheiroJogador -= aposta
        dinheiroBanca += aposta
        print(f'Você ficou com R${dinheiroJogador:.2f} e a Banca tem R${dinheiroBanca:.2f}')
        escolha = str(input('Aposte Par, Impar ou digite um número: ')).strip().upper()[0]

        sorteio = randint(0,36)
        print(f'O número sorteado foi {sorteio}!')
        sleep(1)

        if escolha == 'P' and sorteio%2 == 0 and sorteio != 0:
            dinheiroJogador += 2*aposta
            dinheiroBanca -= 2*aposta
            print(f'Deu PAR! Fazer o que, você acertou! Te paguei R${2*aposta:.2f} e agora tem {dinheiroJogador:.2f}\n'
                  f'E a Banca ficou com R%{dinheiroBanca:.2f}')
        elif escolha == 'I' and sorteio%2 != 0 and sorteio != 0:
            dinheiroJogador += 2*aposta
            dinheiroBanca -= 2*aposta
            print(f'Deu Impar! Fazer o que, você acertou! Te paguei R${2*aposta:.2f} e agora tem {dinheiroJogador:.2f}\n'
                  f'E a Banca ficou com R${dinheiroBanca:.2f}')
        elif escolha == sorteio:
            dinheiroJogador += 30*aposta
            dinheiroBanca -= 30*aposta
            print(f'Acertou em cheio!!! Te paguei R${pagamento:.2f} e agora tem {dinheiroJogador:.2f}\n'
                  f'E a Banca ficou com R${dinheiroBanca:.2f}')
        else:
            print(f'Você errou!!! Perdeu R${aposta:.2f} e a Banca agora tem R${dinheiroBanca:.2f}')


        if dinheiroJogador <= 0:
            print(f'Você perdeu... Sinto muito, só que não kk!!!')
            break
        if dinheiroBanca <= 0:
            print(f'Você ganhou!!! Fazer o que, né...')
            break
        else:
            print(f'Você ainda possui R${dinheiroJogador:.2f} e a banca R${dinheiroBanca:.2f}')
        sair = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if sair == 'S':
            break

print(f'FIM DO PROGRAMA')
