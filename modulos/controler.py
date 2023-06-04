import json
from data.database import Banquinho
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
import json
=======
>>>>>>> Stashed changes
from modulos.operacoes import *
>>>>>>> 8767b513ef33111ad011b289c1bb740819bdabf3
from modulos.modulos import *
from modulos.operacoes import *

<<<<<<< HEAD
class Controle:
=======
class Controle():
>>>>>>> 8767b513ef33111ad011b289c1bb740819bdabf3
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
<<<<<<< HEAD
=======
        
>>>>>>> 8767b513ef33111ad011b289c1bb740819bdabf3

    def sacar(self, quantidade, key):
        operacao = Saque(quantidade)
        self.banquinho.opBancaria(operacao, key)

    def depositar(self, quantidade, key):
        operacao = Deposito(quantidade)
        self.banquinho.opBancaria(operacao, key)

    def solCredito(self, quantidade, key):
        self.banquinho.credito(quantidade, key)

