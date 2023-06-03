import json
import os

class Banquinho:
    def addClient(pessoa, senha):
        pessoaConvert = vars(pessoa)
        senhaConvert = vars(senha)

        '''carregando lista de clientes e atualizando arquivo''' 
        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)

        clientsList.append(pessoaConvert)
        
        with open("clientes.json", "a") as arquivo:
            json.dump(clientsList, arquivo, indent = 4)

        '''criando arquivo individual'''
        nomeArq = pessoa.cpf_cnpj

        with open(nameArq + ".json", "w") as arquivo:
            json.dump(pessoaConvert, arquivo, indent = 4)

        '''arquivo de senhas'''
        with open("senhas.json") as arquivo:
            senhas = json.load(arquivo)

        senhas.append(senhaConvert)


    def rmClient(key):
        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)

        for client in clientsList:
            if client['cpf_cnpj'] == key:
                if client['saldo'] != 0.00:
                    return False
                else:
                    clientsList.remove(client)

                    with open("clientes.json", "w") as arquivo:
                        json.dump(clientsList, arquivo, indent = 4)
        
                    os.remove(key + ".json")

                    break

    def opBancaria(operacao, key):
        '''pegando o valor da operacao'''
        if operacao.tipo == "Saque":
            op = -operacao.valor
        else:
            op = operacao.valor
        
        '''carregando arquivo e atualizando saldo'''
        with open(key + ".json") as arquivo:
            cliente = json.load(arquivo)

        saldo = cliente['saldo'] + op 
        cliente['saldo'] = saldo
        
        '''adicionando operacao na lista de operacoes'''
        cliente['operacoes'].append(operacao)

        with open(key + ".json", "w") as arquivo:
            json.dump(cliente, arquivo, indent = 4)

        '''mexendo na lista geral'''

        
    def solCredito(dados):
        with open("pedidosDeCredito.json") as arquivo:
            pedidos = json.load(arquivo)

        pedidos.append(dados)

        with open("pedidosDeCredito.json", "a") as arquivo:
            json.dump(pedidos, arquivo, indent = 4)

    def listar(key):
        with open(key + ".json") as arquivo:
            op = json.load(arquivo)

        print(json.dump(op, indent = 4))
