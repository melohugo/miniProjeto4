class Saque():
    def __init__(self, valor):
        self.tipo = "Saque"
        self.valor = int(valor)


class Deposito():
    def __init__(self, valor):
        self.tipo = "Deposito"
        self.valor = int(valor)

class PagProg():
    def __init__(self, data, valor):
        self.tipo = "Pagamento programado"
        self.valor = valor
        self.data = data

