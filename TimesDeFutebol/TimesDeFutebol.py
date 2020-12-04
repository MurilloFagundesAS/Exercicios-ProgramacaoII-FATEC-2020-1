jogos = [0, 0, 0, 0, 0]
contador = 0
soma = 0

for i in range(0, 5):
    time = str(input('Você deseja salvar a pontuação de qual time? ')).upper().strip()
    if time == 'CORINTIANS':
        gols = int(input('O Corintians fez quantos gols? '))
        jogos[0] += gols
        contador+=1
        soma += gols
    elif time == 'SÃO PAULO' or time == 'SAO PAULO':
        gols = int(input('O São Paulo fez quantos gols? '))
        jogos[1] += gols
        contador += 1
        soma += gols
    elif time == 'PALMEIRAS':
        gols = int(input('O Palmeiras fez quantos gols? '))
        jogos[2] += gols
        contador += 1
        soma += gols
    elif time == 'SANTOS':
        gols = int(input('O Santos fez quantos gols? '))
        jogos[3] += gols
        contador += 1
        soma += gols
    elif time == 'FLAMENGO':
        gols = int(input('O Flamengo fez quantos gols? '))
        jogos[4] += gols
        contador += 1
        soma += gols
    else:
        print('Você digitou um número errado! Tente novamente...')
        continue

media = soma/contador
print(f'A media de pontos é {media}!!!')

maior = max(jogos)

print()
if maior == jogos[0]:
    print(f'A maior pontuação foi de {jogos[0]} do Corintians')
elif maior == jogos[1]:
    print(f'A maior pontuação foi de {jogos[1]} do São Paulo')
elif maior == jogos[2]:
    print(f'A maior pontuação foi de {jogos[2]} do Palmeiras')
elif maior == jogos[3]:
    print(f'A maior pontuação foi de {jogos[3]} do Santos')
elif maior == jogos[4]:
    print(f'A maior pontuação foi de {jogos[4]} do Flamengo')