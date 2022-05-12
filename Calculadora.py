import math
import time


class Calculadora:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def Soma(self):
        print(f'{self.val1} + {self.val2} = {self.val1 + self.val2}')

    def Subtracao(self):
        print(f'{self.val1} - {self.val2} = {self.val1 - self.val2}')

    def Mult(self):
        print(f'{self.val1} x {self.val2} = {self.val1*self.val2}')

    def Div(self):
        print(f'{self.val1} / {self.val2} = {self.val1/self.val2}')

    def Pot(self):
        print(f'{self.val1}^{self.val2} = {math.Pow(self.val1, self.val2)}')

    def Raiz(self):
        print(f'{self.val1}^1/{self.val2} = {math.Pow(self.val1, 1/self.val2)}')
