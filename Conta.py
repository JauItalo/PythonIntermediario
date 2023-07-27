class Conta:
    def __init__(self, titular, numero):
        self.saldo = 0.0
        self.numero = numero
        self.titular = titular

    @property
    def saldo(self):
            return self._saldo

    @saldo.setter
    def saldo(self, saldo):
            if (saldo < 0):
                print("Ta sem dinheiro, mané")
            else:
                self._saldo = saldo

    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def depositar(self, valor):
        self.saldo+=valor

    def extrato(self):
        print("Cliente: ",self.titular, " Saldo atual: ",self.saldo)

