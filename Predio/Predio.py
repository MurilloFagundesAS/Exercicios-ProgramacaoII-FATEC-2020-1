from random import randint
import math

print(f'Jogo do Prédio')

distanciaPredio = randint(5, 100)
print(f'Você está a {distanciaPredio} metros do prédio')

andar = randint(1, 15)
print(f'Acerte a janela do andar {andar}º!')

angulo = float(input(f'Em qual ângulo que você vai atirar? '))
d = math.sqrt((andar * 3) ** 2 + distanciaPredio ** 2)

hMax = andar * 3
hMin = (andar - 1) * 3

x = d*math.cos(angulo)
y = d * math.cos(angulo)
