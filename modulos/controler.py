from data.database import Banquinho
from operacoes import *
from modulos import *

class Controle():
    def __init__():
        banquinho = Banquinho()

    def verifCpf(cpf, key):
        with open("senhas.json") as arquivo:
            senha = json.load(arquivo)

        for verificador in senha:
            if verificador['senha'] == key and verificador['cpf_cnpj'] == cpf:
                return True
            else:
                return False

    def addPessoa(self, nome, key, endereco, telefone, senha, tipo)
        cliente = Cliente(tipo, nome, key, endereco, telefone)

        clienteConvert = vars(cliente)

        chave = Senha(key, senha)

        chaveConvert = vars(chave)
        
        self.banquinho.addClient(clienteConvert, chave)

    def rmPessoa(self, key)
        banquinho.rmClient(key)
        

    def sacar(self, quantidade, key):
        operacao = Saque(quantidade)
        operacaoConvert = vars(operacao)
        self.banquinho.opBancaria(operacaoConvert, key)

    def depositar(self, quantidade, key):
        operacao = Deposito(quantidade)
        operacaoConvert = vars(operacao)
        self.banquinho.opBancaria(operacaoConvert, key)

