"Sonic the Headgehog 2 - 1992"
class PersonagemSonic:
    def __init__(self):
        self.velocidade = 0
        self.ataque = False
        self.vida = 1
        self.parado = True

    def correr(self):
        if self.parado == True:
            self.velocidade += 1
            self.parado = False
        else:
            self.parado = True
            self.velocidade += 0

    def atacar(self):
        self.ataque = True

    def apanhou(self):
        self.vida -= 1


class PersonagemTales:
    def __init__(self):
        self.voando = False
        self.vida = 1
        self.ataque = False

    def voar(self):
        if self.voando == False:
            self.voando = True
        else:
            self.voando = False

    def apanhou(self):
        self.vida -= 1

    def atacar(self):
        if self.ataque == False:
            self.ataque = True
        else:
            self.ataque = False


class Moeda:
    def __init__(self):
        self.quantidade = 10
        self.girando = True
        self.apanhou = False
        self.perdeuMoeda = False

    def pegouMoeda(self):
        self.quantidade -= 1

    def levouDano(self):
        if self.apanhou == True:
            self.apanhou = False
            self.perdeuMoeda = True
        else:
            pass

class InimigoPiranha:
    def __init__(self):
        self.pulo = False
        self.vida = 1
        self.liberto = False

    def pulou(self):
        if self.pulo == False:
            self.pulo = True
        else:
            self = False

    def apanhou(self):
        self.vida -= 1
        self.liberto = True

class InimigoVespa:
    def __init__(self):
        self.vida = 1
        self.liberto = False
        self.ataque = False

    def apanhou(self):
        self.liberto = True
        self.vida -= 1

    def atacando(self):
        self.ataque = True


# Sonic
sonic = PersonagemSonic()
# Tales
tales = PersonagemTales()
# Moedas coletáveis
moeda = Moeda()
# Piranha
piranha = InimigoPiranha()
# Vespa
vespa = InimigoVespa()


print(f'Vida da piranha: {piranha.vida}')
piranha.apanhou()
print(f'Vida da piranha: {piranha.vida}')
