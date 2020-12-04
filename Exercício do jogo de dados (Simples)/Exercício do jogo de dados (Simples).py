import random
x = int(input("Escolha um número de 1 a 6:"))
voceGanhou: bool

dado = random.randint(1, 6)
if x == dado:
    voceGanhou = True
else:
    voceGanhou = False
print(f"{voceGanhou}")