# 2. Classes e Objetos


from classe import Conta

# Criando um Objeto: coloque entre parentesis como se faz com as chamadas de funções
#guardar os retornos dentro de uma variável de referência, assim como o java

conta1 = Conta(123, "Edi", 100.0, 1000.0)

conta2 = Conta(234, "Edinha", 200.0, 1050.0)

#referenciando
print(conta1.numero)
print(conta2.numero)