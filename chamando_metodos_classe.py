# 4. Encapsulamento
# Sem atributos privados eu posso alterar valores

from metodos_da_classe import ContaCorrente


conta = ContaCorrente(123, "Edi", 1000.00, 100.00)


print(conta.codigo_banco)

print(ContaCorrente.codigo_banco())

codigos = ContaCorrente.codigos_bancos()

print(codigos['Caixa'])


