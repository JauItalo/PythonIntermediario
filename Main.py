class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1._nome, 3232,0)

print(conta.titular,":Numero:",conta.numero, "Seu Saldo: ", conta.saldo)