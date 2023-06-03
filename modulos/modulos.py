class Cliente():
    def __init__(self, tipo, nome, key, endereco, telefone, senha):
        self.nome = nome
        
        self.tipo = tipo
        self.cpf_cnpj = key
        self.endereco = endereco
        self.telefone = telefone
        self.saldo = 0.00

class Senha():
    def __init__(self, key, senha)
        self.cpf_cnpj = key
        self.senha = senha

class Cliente(Pessoa):
    def __init__(self, nome, endereco, telefone, senha, cpf):
        super().__init__(nome, endereco, telefone, senha)
        self.cpf = cpf

class Empresa(Pessoa):
    def __init__(self, nome, endereco, telefone, senha, cnpj):
        super().__init__(nome, endereco, telefone, senha)
        self.cnpj = cnpj

class Gerente(Pessoa):
     def __init__(self, nome, endereco, telefone, senha, idG):
        super().__init__(nome, endereco, telefone, senha)
        self.id = idG

