# 3. Implementando Métodos
# Passagem de parâmetros, sempre chame o self


class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite): #Construtor
        print("Construindo Objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self): #chame self sempre!
        print("O saldo do titular {} é: R$ {:.2f}".format(self.titular, self.saldo))

#none = o null do Java