# 4. Encapsulamento
# Sem atributos privados eu posso alterar valores

from metodos_privados import ContaCorrente


conta = ContaCorrente(123, "Edi", 1000.00, 100.00)


print(conta.saldo)

conta.saca(101.0)

print(conta.saldo)

conta.saca(1.00)

print(conta.saldo)

print(conta.__pode_sacar(1000))