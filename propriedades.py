# 5. Usando propriedades

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self): #outra forma de escrever um get
        print("Chamando @proprety nome() - get")
        return self.__nome.title() #title assegura que a primeira letra será maiuscula

    @nome.setter
    def nome(self, nome): #outra forma de escrever um set
        print("Chamando @proprety nome() - set")
        self.__nome = nome

