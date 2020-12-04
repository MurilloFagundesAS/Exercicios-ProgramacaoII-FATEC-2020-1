class Fusca():
    def __init__(self, cor):
        self.porta_aberta = False
        self.velocidade_atual = 0
        self.potencia_motor = 0
        self.ligado = False
        self.cor = cor
        print(f'Seu fusca {cor} está pronto para usar!')

    def acelerar(self):
        if self.ligado == True:
            if self.porta_aberta == False:
                self.velocidade_atual += 10
                print(f'Você está a {self.velocidade_atual}km/h!')
            else:
                print('A porta está aberta!')
        else:
            print('Boa tentativa, mas o carro não está ligado...')

    def frear(self):
        if self.ligado == True:
            if self.velocidade_atual <=0:
                self.velocidade_atual = 0
                print(f'Você já está parado!')
            else:
                self.velocidade_atual -=5
                print(f'Você está a {self.velocidade_atual}km/h!')
        else:
            print('Boa tentativa, mas o carro não está ligado...')

    def abrir_porta(self):
        if self.porta_aberta == True:
            self.porta_aberta = False
            print('Você fechou a porta!')
        else:
            self.porta_aberta = True
            print('Você abriu a porta!')

    def ligar(self):
        if self.velocidade_atual == 0:
            if self.ligado == True:
                self.ligado = False
                print('Você desligou o carro!')
            else:
                self.ligado = True
                print(f'Você ligou o carro {self.cor}!')
        else:
            print(f'Você está a {self.velocidade_atual}km/h! Desacelere um pouco mais para parar')


carro1 = Fusca("azul")
carro2 = Fusca("vermelho")
herbie = Fusca('bege')

carro1.ligado
carro1.abrir_porta()
carro1.acelerar()
carro1.abrir_porta()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.ligar()
carro1.frear()
carro1.ligar()