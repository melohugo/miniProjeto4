import json
from database import Banquinho
from cliente import *
from operacoes import *

class Controle:
    def __init__(self):
        self.banquinho = Banquinho()

    def verifCpf(self, cpf, key):
        return self.banquinho.verificador(cpf, key)

    def addPessoa(self, nome, key, endereco, telefone, senha, tipo):
        cliente = Cliente(tipo, nome, key, endereco, telefone)
        chave = Senha(key, senha)
        self.banquinho.addClient(cliente, chave)

    def rmPessoa(self, key):
        return self.banquinho.rmClient(key)

    def sacar(self, quantidade, key):
        operacao = Saque(quantidade)
        return self.banquinho.opBancaria(operacao, key)

    def depositar(self, quantidade, key):
        operacao = Deposito(quantidade)
        return self.banquinho.opBancaria(operacao, key)

    def solCredito(self, quantidade, key):
        self.banquinho.credito(quantidade, key)

    def programarPag(self, quantidade, data, key):
        self.banquinho.pagProg(quantidade, data, key)

    def atualizarPagamento(self, data):
        self.banquinho.atualizarPagProg(data)