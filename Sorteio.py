import random
class Sorteio:

    jogador = []

    resultado = []

    def __init__(self, jogador):
        self.jogador.append(jogador)
        print(f'{jogador} foi inserido')

    def RealizarSorteio(self):
        self.jogador.sort()
        for i in range(0, len(self.jogador), 2):
            self.resultado.append(f'{self.jogador[i]} x {self.jogador[i+1]}')
        for i in range(0, len(self.jogador), 2):
            return self.resultado[i]