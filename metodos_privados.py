# 6. Métodos privados e estáticos

class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

# Fiz assim!
#    def saca(self, valor):
#        if valor <= self.__saldo:
#            print("Valor: {}".format(valor))
#            print("Limite: {}".format(self.__limite))
#            if valor <= self.__limite:
#                self.__saldo -= valor
#            else:
#                print("O valor excede o limite permitido")
#        else:
#            print("Saldo insuficiente")

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor R${} passou o limite R${}".format(valor, self.__limite))

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def extrato(self):
        print("O saldo do titular {} é: R$ {:.2f}".format(self.__titular, self.__saldo))

    def saldo(self):
        print("O saldo é: R$ {:.2f}".format(self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite;


