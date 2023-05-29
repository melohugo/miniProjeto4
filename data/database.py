import json
import os

class Db:
    def addClient(pessoa, tipo):
        pessoaConvert = vars(pessoa)
        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)

        clientsList.append(pessoaConvert)
        
        with open("clentes.json", "a") as arquivo:
            json.dump(clientsList, arquivo, indent = 4)

        if tipo == "empresa":
            nameArq = pesoa.cnpj
        else:
            nameArq = pessoa.cpf

        with open(nameArq + ".json", "w") as arquivo:
            json.dump(pessoaConvert, arquivo, indent = 4)

        
    def rmClient(key, tipo):
        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)

        for client in clientsList:
            if client[tipo] == key:
                clientsList.remove(client)

        with open("clientes.json", "w") as arquivo:
            json.dump(clientsList, arquivo, indent = 4)
        
        os.remove(key + ".json")

    def opBancaria(operacao, key):
        with open(key + ".json", "a") as arquivo:
            json.dump(operacao, arquivo, indent = 4)
        
    def solCredito(dados):
        with open("pedidosDeCredito.json") as arquivo:
            pedidos = json.load(arquivo)

        pedidos.append(dados)

        with open("pedidosDeCredito.json", "a") as arquivo:
            json.dump(pedidos, arquivos, indent = 4)

    def listar(key):
        with open(key + ".json") as arquivo:
            op = json.load(arquivo)

        print(json.dump(op, indent = 4))
