import json
from data.database import Banquinho
from modulos.cliente import *
from modulos.operacoes import *

class Controle:
    def __init__(self):
        self.banquinho = Banquinho()

    def verifCpf(self, cpf, key):
        return self.banquinho.verificador(cpf, key)

    def addPessoa(self, nome, key, endereco, telefone, senha, tipo):
        cliente = Cliente(tipo, nome, key, endereco, telefone, senha)
        chave = Senha(key, senha)
        self.banquinho.addClient(cliente, chave)

    def rmPessoa(self, key):
        self.banquinho.rmClient(key)

    def sacar(self, quantidade, key):
        operacao = Saque(quantidade)
        self.banquinho.opBancaria(operacao, key)

    def depositar(self, quantidade, key):
        operacao = Deposito(quantidade)
        self.banquinho.opBancaria(operacao, key)

    def solCredito(self, quantidade, key):
        self.banquinho.credito(quantidade, key)

    def programarPag(self, quantidade, data, key):
        self.banquinho.pagProg(quantidade, data, key)

    def atualizarPagamento(self, data):
        self.banquinho.atualizarPagProg(data)
