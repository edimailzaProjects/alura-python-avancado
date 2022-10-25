# 1. O problema do paradígma Procedural
# Possíveis ações em uma Conta

# Apesar da "forçada de barra", esses métodos expostos dessa forma são muito frágeis, exemplo:
# eu posso depositar sem chamar o método deposita, apenas colocando conta["saldo"] = conta["saldo"] + 100.0
# eu poderia colocar esses métodos separados em arquivos diferentes
# Imagine o caos se em vez de 4 funções, tivéssemos 1000

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta #Python exige return

def deposita(conta, valor):
    conta["saldo"] += valor #eu preciso acessar a conta através da chave saldo

def saca(conta, valor):
    conta["saldo"] -= valor #eu preciso acessar a conta através da chave saldo

def extrato(conta):
    print("O saldo é: R$ {:.2f}".format(conta["saldo"]))