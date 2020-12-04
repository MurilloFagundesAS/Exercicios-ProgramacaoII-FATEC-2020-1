from random import randint
jogar: int
cartaNova: int

jogar = int(input("Digite 1 para jogar: "))
cartaNova = 0
total = 0

while jogar == 1:
    cartaNova = randint(1,10)
    print(f"A carta tirada foi {cartaNova}")
    total = total + cartaNova
    print(f"Você tem {total} pontos")

    if total <= 10:
        print("Sem dúvida compre mais uma carta!")
        jogar = int(input("Digite 1 para continuar apostando:"))
    elif total>10 and total<=15:
        print(f"Há risco, mas aconselho comprar mais uma carta...")
        jogar = int(input("Digite 1 para continuar apostando: "))
    elif total>15 and total<=20:
        print(f"Aconselho parar de jogar!")
        jogar = int(input("Digite 1 para continuar apostando: "))
    elif total == 21:
        print(f"Você já venceu, não precisa mais comprar!!!")
        jogar += 7
    else:
        print(f"Você perdeu!!!")
        jogar += 7
    print()