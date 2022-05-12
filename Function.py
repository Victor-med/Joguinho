class Banco:
    def __init__(self, nome, nascimento, numconta, saldo):
        self.nome = nome
        self.nascimento = nascimento
        self.numconta = numconta
        self.saldo = saldo

    def Depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
            print('Deposito feito com sucesso!')
        else:
            print('Erro! Valor inválido')

    def Sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print('Saque efetuado com sucesso!')
        else:
            print('Erro! Saldo insuficiente!')

    def Extrato(self):
        print(f'R${self.saldo}')

    def ConsultaConta(self):
        print(f"""Nome: {self.nome} 
Data de Nascimento: {self.nascimento} 
Número da conta: {self.numconta}""")

    def Pagamento(self, valor_boleto):
        if self.saldo >= valor_boleto:
            self.saldo -= valor_boleto
            print('Pagamento efetuado!')
        else:
            print(f'Erro! Saldo insuficiente de R${self.saldo} para pagar R${valor_boleto}')