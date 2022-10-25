# 4. Encapsulamento
# Sem atributos privados eu posso alterar valores

from atributos_privados import ContaCorrente


conta = ContaCorrente(123, "Edi", 10.00, 1000.00)

#print("Antes: {:.2f}".format(conta.saldo))

#conta.saldo = 60.0 #Esse tipo de operação só deveria ser possível através do método deposita() ou saca()
#para isso, colocamos __ no atributo
#print("Depois: {:.2f}".format(conta.saldo))

#após isso, eu consigo acessar unicamente os métodos deposita() ou saca() se eu quiser alterar o saldo

print(conta.saldo())

conta.deposita(1000.50)

print(conta.saldo())
