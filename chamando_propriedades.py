# 5. Usando Propriedades


from propriedades import Cliente
from getters_setters_properties import ContaCorrente

cliente = Cliente("Edi")

cliente.nome

cliente.nome = "Edimailza"

conta = ContaCorrente(123, "Edi", 100.0, 2000.0)

print(conta.limite)

conta.limite = 3000.0

print(conta.limite)