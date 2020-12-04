total = int(input("Quanto Você Tem?"))

if total <= 10:
    print(f"Você tem {total} pontos. Sem dúvida compre mais uma carta!")
elif total>10 and total<=15:
    print(f"Você tem {total} pontos. Há risco, mas aconselho comprar mais uma carta...")
elif total>15 and total<=20:
    print(f"Você tem {total} pontos. Aconselho parar de jogar!")
elif total == 21:
    print(f"Você tem {total} pontos. Você já venceu, não precisa mais comprar!!!")
else:
    print(f"Você tem {total} pontos. Você perdeu!!!")
