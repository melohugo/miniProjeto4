class Saque:
    def __init__(self, valor):
        self.tipo = "Saque"
        self.valor = valor


class Deposito:
    def __init__(self, valor):
        self.tipo = "Deposito"
        self.valor = valor


class PagProg:
    def __init__(self, data, valor):
        self.tipo = "Pagamento programado"
        self.valor = valor
        self.data = data

class SolicitarCredito:
    def __init__(self, nome, tipo, key, saldo, quantidade):
        self.nome = nome
        self.tipo = tipo
        self.cpf_cnpj = key
        self.saldo = saldo
        self.pedidoDeCredito = quantidade