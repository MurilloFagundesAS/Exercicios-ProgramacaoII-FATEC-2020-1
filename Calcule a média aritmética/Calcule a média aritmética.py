media: float

nota1 = int(input("Qual a primeira nota?"))
nota2 = int(input("Qual a segunda nota?"))
nota3 = int(input("Qual a terceira nota?"))
nota4 = int(input("Qual a quarta nota?"))

media = (nota1 + nota2 + nota3 + nota4)/4
if media > 6:
    print(f"Média ={media}. Passou, meus parabéns!!!")
else:
    print(f"Média = {media}. Meu amigo, não foi dessa vez...")