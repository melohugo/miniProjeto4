class Cliente:
    def __init__(self, tipo, nome, key, endereco, telefone, senha):
        self.nome = nome
        self.tipo = tipo
        self.cpf_cnpj = key
        self.endereco = endereco
        self.telefone = telefone
        self.saldo = 0.00
        self.operacoes = []
        self.senha = senha


class Senha:
    def __init__(self, key, senha):
        self.cpf_cnpj = key
        self.senha = senha