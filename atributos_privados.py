# 4. Encapsulamento

class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero #quando coloco __ eu estou dizendo que esses atributos são privados e não preciso iniciar com a palavra private
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def extrato(self): #chame self sempre!
        print("O saldo do titular {} é: R$ {:.2f}".format(self.__titular, self.__saldo))

    def saldo(self):
        print("O saldo é: R$ {:.2f}".format(self.__saldo))

