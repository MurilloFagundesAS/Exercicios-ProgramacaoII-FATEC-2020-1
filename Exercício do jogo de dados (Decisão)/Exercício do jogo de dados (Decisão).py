import random
x = int(input("Escolha um número de 1 a 6:"))
dado = random.randint(1, 6)

if x == dado:
    print(f"Número escolhido: {x} \n"
          f"Número sorteado: {dado} \n"
          f"PARABÉNS. VOCÊ VENCEU!!!")
else:
    print(f"Número escolhido: {x} \n"
          f"Número sorteado: {dado} \n"
          f"QUE PENA. VOCÊ PERDEU...")