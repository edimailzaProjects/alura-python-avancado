# 1. O problema do paradígma Procedural
# Chamando as funções

from funcoes_conta import cria_conta, deposita, saca, extrato

conta = cria_conta(789, "Ed", 10.50, 1050.0)

deposita(conta, 0.10) # diferente do java, não precisa de set e get

extrato(conta)

saca(conta, 0.10)

extrato(conta)

