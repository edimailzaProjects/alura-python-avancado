# 3. Implementando Métodos

from implementa_metodos import ContaCorrente

conta1 = ContaCorrente(123, "Edi", 100.0, 1000.0)

print(conta1.extrato())
print(conta1.deposita(20.0))
print(conta1.extrato())
print(conta1.saca(10.0))
print(conta1.extrato())

conta2 = ContaCorrente(234, "Edinha", 200.0, 1050.0)

print(conta2.extrato())
print(conta2.deposita(200.0))
print(conta2.extrato())