# 5. Usando Propriedades


from getters_setters import ContaCorrente


conta1 = ContaCorrente(123, "Edi", 10.00, 1000.00)


print(conta1.get_limite())
conta1.set_limite(2000.0)
print(conta1.get_limite())
