from data.database import Banquinho

class Controle():
    def __init__():
        banquinho = Banquinho()

    def verifCpf(cpf, key):dados
        with open("senhas.json") as arquivo:
            senha = json.load(arquivo)

        for verificador in senha:
            if verificador['senha'] == key and verificador['cpf'] == cpf:
                return True
            else:
                return False

    def sacar():

    def depositar(quantidade):
        dados = {
                "Operacao": "Deposito",
                "Valor": quantidade
                }
        banquinho.opBancaria(dados)

