# 5. Usando propriedades

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

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    def set_limite(self, novo_limite):
        self.__limite = novo_limite;


