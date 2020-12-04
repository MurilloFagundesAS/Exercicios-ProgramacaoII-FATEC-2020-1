nota = int(input("Digite a Nota:"))
presença = int (input("Digite a Presença:"))
media = 7

passouPresença1 = (nota > media) or (presença == 100)
passouPresença2 = (nota > media) and (presença == 75)
raspandoPresença1 = (nota == media) and (presença > 75)
raspandoPresença2 = (nota == media) or (presença >= 80)
naoPassouPresença1 = (nota < media) and (presença < 75)
naoPassouPresença2 = (nota < media) or (presença < 50)
feraPresença1 = (nota == 10) and (presença == 100)
feraPresença2 = (nota == 10) or (presença == 100)

print(f"passouPresença1 = {passouPresença1} \n"
      f"passouPresença2 = {passouPresença2} \n"
      f"raspandoPresença1 = {raspandoPresença1} \n"
      f"raspandoPresença2 = {raspandoPresença2} \n"
      f"naoPassouPresença1 = {naoPassouPresença1} \n"
      f"naoPassouPresença2 = {naoPassouPresença2} \n"
      f"feraPresença1 = {feraPresença1} \n"
      f"feraPresença2 = {feraPresença2} \n")