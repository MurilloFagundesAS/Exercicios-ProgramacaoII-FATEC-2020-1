from random import randint

x = int(input("Digite um número de 1 a 6: "))

dado = randint(1,6)
acertou = (dado == x)

print(f"Acertou = {acertou}")