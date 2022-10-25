# 6. Métodos privados e estáticos

class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "001" #quando criar, automaticamente será no codigo desse banco

    def deposita(self, valor):
        self.__saldo += valor

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

    @staticmethod
    def codigo_banco(): #para chamar o código eu preciso ter um objeto primeiro e, quando não coloco self significa que é método da classe
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa': '002', 'Bradesco': '003'} #chave, valor
