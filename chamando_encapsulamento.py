# 4. Encapsulamento


from encapsulamento import ContaCorrente


conta1 = ContaCorrente(123, "Edi", 10.00, 1000.00)

conta2 = ContaCorrente(456, "Edinha", 20.00, 2000.00)

valor = 5.0

#Inviável essa operação de transferência. É mais inteligente encapsular e terceirizar para um método de transferência

#print(conta1.saca(valor))

#print(conta1.saldo())

#conta2.deposita(valor)

#print(conta2.saldo())

print(conta2.transfere(valor, conta1))

print(conta1.saldo())