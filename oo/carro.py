"""

Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade:
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear, que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Metodo girar_a_direita
2) Metodo girar_a_esquerda

  N
O   L
  S

    """
import motor


class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return print(self.velocidade)

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
            return print(self.velocidade)
        elif self.velocidade == 1:
            self.velocidade = 0
            return print(self.velocidade)

    '''
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
'''


class Direcao:
    direcao_direita = {'Norte': 'Leste', 'Leste': 'Sul', 'Sul': 'Oeste', 'Oeste': 'Norte'}
    direcao_esquerda = {'Norte': 'Oeste', 'Oeste': 'Sul', 'Sul': 'Leste', 'Leste': 'Norte'}

    def __init__(self, direcao='Norte'):
        self.direcao = direcao

    def girar_a_direita(self):
        self.direcao = self.direcao_direita[self.direcao]
        return print(self.direcao)

    def girar_a_esquerda(self):
        self.direcao = self.direcao_esquerda[self.direcao]
        return print(self.direcao)

    def calcular_direcao(self):
        return print(self.direcao)

    '''
    >>> direção = Direção()
    >>> direção.valor
    'Norte'
    >>> direção.girar_a_direita()
    >>> direção.valor
    'Leste'
    >>> direção.girar_a_direita()
    >>> direção.valor
    'Sul'
    >>> direção.girar_a_direita()
    >>> direção.valor
    'Oeste'
    >>> direção.girar_a_direita()
    >>> direção.valor
    'Norte'
    >>> direção.girar_a_esquerda()
    >>> direção.valor
    'Oeste'
    >>> direção.girar_a_esquerda()
    >>> direção.valor
    'Sul'
    >>> direção.girar_a_esquerda()
    >>> direção.valor
    'Leste'
    >>> direção.girar_a_esquerda()
    >>> direção.valor
    'Norte'
    '''


class Carro:
    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def velocidade(self):
        print(self.motor.velocidade)




'''
    >>> carro = Carro(direção, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0

    >>> carro.calcular_direção()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direção()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direção()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direção()
    >>> 'Oeste'
'''
if __name__ == '__main__':

    carro = Carro(direcao=Direcao(), motor=Motor())
    print(carro.motor.velocidade)
    carro.motor.acelerar()
    carro.motor.acelerar()
    carro.motor.acelerar()
    carro.motor.frear()
    carro.motor.frear()

    carro.direcao.calcular_direcao()
    carro.direcao.girar_a_direita()
    carro.direcao.girar_a_direita()
    carro.direcao.girar_a_direita()
    carro.direcao.girar_a_direita()
    carro.direcao.girar_a_esquerda()
    carro.direcao.girar_a_esquerda()
    carro.direcao.girar_a_esquerda()
    carro.direcao.girar_a_esquerda()


