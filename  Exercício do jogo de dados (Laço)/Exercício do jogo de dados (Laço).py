import random

x = int(input("Digite 1 se deseja para jogar:"))

while x == 1:
    y = int(input("Digite um Número de 1 a 6:"))
    dado = random.randint(1,6)
    if y == dado:
        print(f"Você Ganhou!!! \n"
              f"Valor Digitado: {y} \n"
              f"Valor do Dado: {dado}")
    else:
        print(f"Você Perdeu!!! \n"
              f"Valor Digitado: {y} \n"
              f"Valor do Dado: {dado}")
    print()
    x = int(input("Digite 1 se Deseja Jogar Outra Vez:"))

print(f"Você Não Quis Jogar De Novo,")