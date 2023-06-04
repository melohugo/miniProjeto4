import json
import os
from cliente import *
from operacoes import *

class Banquinho:
    def addClient(self, pessoa, senha):
        pessoaConvert = vars(pessoa)
        senhaConvert = vars(senha)

        ##carregando lista de clientes e atualizando arquivo##

        if os.path.isfile("clientes.json"):
            with open("clientes.json", "r") as arquivo:
                clientsList = json.load(arquivo)
        else:
            clientsList = []

        clientsList.append(pessoaConvert)

        with open("clientes.json", "w") as arquivo:
            json.dump(clientsList, arquivo, indent=4)

        ##criando arquivo individual##

        nomeArq = pessoa.cpf_cnpj

        with open( nomeArq + ".json", "w") as arquivo:
            json.dump(pessoaConvert, arquivo, indent=4)

        ##arquivo de senhas##

        if os.path.isfile("senhas.json"):
            with open("senhas.json", "r") as arquivo:
                senhas = json.load(arquivo)
        else:
            senhas = []

        senhas.append(senhaConvert)

        with open("senhas.json", "w") as arquivo:
            json.dump(senhas, arquivo, indent = 4)

    def rmClient(self, key):

        ##deletando cliente##

        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)
        
        for client in clientsList:
            if client['cpf_cnpj'] == key:
                if client['saldo'] == 0.00:
                    clientsList.remove(client)

                    with open("clientes.json", "w") as arquivo:
                        json.dump(clientsList, arquivo, indent=4)

                    os.remove( key + ".json")

                    break
                else:
                    print("operacao invalida")
                    break

        ##deletando senha##

        with open("senhas.json") as arquivo:
            senhasList = json.load(arquivo)

        for senha in senhasList:
            if senha['cpf_cnpj'] == key:
                senhasList.remove(senha)
                break

        with open("senhas.json", "w") as arquivo:
            json.dump(senhasList, arquivo, indent = 4)

    def opBancaria(self, operacao, key):

        ##pegando o valor da operacao##

        if operacao.tipo == "Saque":
            op = -operacao.valor
        else:
            op = operacao.valor

        ##carregando arquivo e atualizando saldo##
        with open( key + ".json") as arquivo:
            cliente = json.load(arquivo)

        saldo = cliente['saldo'] + op
        cliente['saldo'] = saldo

        ##adicionando operacao na lista de operacoes##
        cliente['operacoes'].append(vars(operacao))

        with open( key + ".json", "w") as arquivo:
            json.dump(cliente, arquivo, indent=4)

    def credito(self, quandidade, key):

        ##carregando arquivo##

        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)

        ##pegando dados do cliente##

        for client in clientsList:
            if client['cpf_cnpj']:
                nome = client['nome']
                tipo = client['tipo']
                key = client['cpf_cnpj']
                saldo = client['saldo']

                break
        
        ##criando e convertendo a classe SolicitarCredito##

        solicitacao = SolicitarCredito(nome, tipo, key, saldo, quandidade)
        solicitacaoConvert = vars(solicitacao)

        ##carregando/criando arquivo dos pedidos##

        if os.path.isfile("pedidosDeCredito.json"):
            with open("pedidosDeCredito.json", "r") as arquivo:
                pedidos = json.load(arquivo)
        else:
            pedidos = []

        ##atualizando lista e escrevendo no arquivo##

        pedidos.append(solicitacaoConvert)

        with open("pedidosDeCredito.json", "w") as arquivo:
            json.dump(pedidos, arquivo, indent=4)

    def listar(self, key):
        with open(key + ".json") as arquivo:
            op = json.load(arquivo)

        print(json.dumps(op, indent=4))

    def verificador(self, cpf, key):

        ##carregando arquivo das senhas##

        with open("senhas.json") as arquivo:
            senha = json.load(arquivo)

        ##fazendo confirmação de senha e cpf/cnpj##

        for verificador in senha:
            if verificador['senha'] == key and verificador['cpf_cnpj'] == cpf:
                return True
        return False
