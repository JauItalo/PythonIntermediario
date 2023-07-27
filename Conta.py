class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular


        @property
        def get_saldo(self):
            return self._saldo
        @saldo.setter
        def set_saldo(self, saldo):
            if (saldo < 0):
                print("Ta sem dinheiro, mané")
            else:
                self._saldo = saldo
