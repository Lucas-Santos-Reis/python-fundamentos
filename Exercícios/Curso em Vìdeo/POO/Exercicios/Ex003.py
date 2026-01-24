class ContaBancaria:
    '''
    Cria uma conta bancária que permite a realização de saques e depósitos
    '''

    def __init__(self, id:int, nome:str, saldo:float = 0): #atributos da conta
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'A conta {self.id} de {self.titular} possui R$ {self.saldo:,.2f} disponível. '
    
    def deposito(self, valor:float):
        self.saldo += valor
        print(f'Você realizou o seu depósito de R${valor:,.2f} com sucesso!\nSeu saldo atual é de R${self.saldo:,.2f}.')

    def saque(self, valor:float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Seu saque de R${valor:,.2f} foi autorizado e realizado com sucesso!\nSeu saldo atual é de R${self.saldo:,.2f}')
        else:
            print(f'Saque NEGADO, valor em saldo é INSUFICIENTE!\nSaldo atual R${self.saldo:,.2f}\nTentativa de saque foi de R${valor:,.2f}')

conta_1 = ContaBancaria(364, 'Lucas', 5350)
conta_1.saque(52350)
conta_1.deposito(1325)
print(conta_1)