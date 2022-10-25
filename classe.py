# 2. Classes e Objetos
# Para criar um objeto eu preciso definir suas características na classe


class Conta: #precisa se dois pontos, assim como as funções
    def __init__(self, numero, titular, saldo, limite): #função construtora
        print("Construindo Objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

