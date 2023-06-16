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
        
    def clienteAtual(self, key):
        self.banquinho.atualizaCpf(key)

    def mostraClienteAtual(self):
        return self.banquinho.checaCpf()
    
    def mostrarPedidos(self):
        return self.banquinho.pedidosDeCredito()
    
    def mostrarSaldo(self, key):
        return self.banquinho.saldo(key)
    
    def atualizarSenha(self, key, novaSenha):
        self.banquinho.trocaSenha(key, novaSenha)

    def atualizarCredito(self, key):
        valor = self.banquinho.verificarCredito(key)
        deposito = self.depositar(valor, key)
