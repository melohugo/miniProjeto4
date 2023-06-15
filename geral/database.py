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
            
    def deletarSenha(self, key):
            
    ##deletando senha##

        with open("senhas.json") as arquivo:
         senhasList = json.load(arquivo)

        for senha in senhasList:
            if senha['cpf_cnpj'] == key:
                senhasList.remove(senha)
                break

        with open("senhas.json", "w") as arquivo:
            json.dump(senhasList, arquivo, indent = 4)

    def rmClient(self, key):

        ##deletando cliente##

        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)
        
        for client in clientsList:
            if client['cpf_cnpj'] == key:
                if client['saldo'] == 0.00:
                    
                    self.deletarSenha(key)

                    clientsList.remove(client)

                    with open("clientes.json", "w") as arquivo:
                        json.dump(clientsList, arquivo, indent=4)

                    os.remove(key + ".json")

                    return True
                else:
                    return False

        

    def opBancaria(self, operacao, key):

        ##pegando o valor da operacao##

        if operacao.tipo == "Saque":
            op = -operacao.valor
        else:
            op = operacao.valor

        ##carregando arquivo e atualizando saldo##
        with open( key + ".json") as arquivo:
            cliente = json.load(arquivo)
        
                ##atendendo requisito de saque##
        if cliente['saldo'] + op < 0.00:
            return False

        saldo = cliente['saldo'] + op
        cliente['saldo'] = saldo

        ##adicionando operacao na lista de operacoes##
        cliente['operacoes'].append(vars(operacao))

        with open( key + ".json", "w") as arquivo:
            json.dump(cliente, arquivo, indent=4)

        ##atualizando arquivo com todos os clientes##
        with open("clientes.json", "r") as arquivo:
            clientsList = json.load(arquivo)

        for cliente in clientsList:
            if cliente['cpf_cnpj'] == key:
                cliente['saldo'] = saldo
                break

        with open("clientes.json", "w") as arquivo:
            json.dump(clientsList, arquivo, indent = 4)

        return True

    def credito(self, quandidade, key):

        ##carregando arquivo##

        with open("clientes.json") as arquivo:
            clientsList = json.load(arquivo)

        ##pegando dados do cliente##

        for client in clientsList:
            if client['cpf_cnpj'] == key:
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
        with open( key + ".json") as arquivo:
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

    def pagProg(self, quantidade, data, key):

        ##carregando arquivo pessoal e convertendo pagamento programado para json##
        with open( key + ".json", "r") as arquivo:
            clientList = json.load(arquivo)

        pagamento = PagProg(data, quantidade)
        pagamentoConvert = vars(pagamento)

        ##adicionando pagamento programado na lista de operações do cliente e atualizando arquivo##
        clientList['operacoes'].append(pagamentoConvert)

        with open( key + ".json", "w") as arquivo:
            json.dump(clientList, arquivo, indent = 4)

    def atualizarPagProg(self, data):

        ##carregando arquivo geral e percorrendo ele##
        with open("clientes.json", "r") as arquivo:
            clientsList = json.load(arquivo)

        for client in clientsList:
            key = client['cpf_cnpj']
            
            ##carregando arquivo pessoal e verificando pagamento programado##
            with open( key + ".json", "r") as arquivo:
                cliente = json.load(arquivo)

            for operacao in cliente['operacoes']:
                if operacao['tipo'] == "Pagamento programado" and operacao['data'] == data:
                    cliente['saldo'] = cliente['saldo'] - operacao['valor']

                    operacao['data'] = operacao['data'] + " pago"
                    
                    ##debitando do arquivo geral##
                    client['saldo'] = client['saldo'] - operacao['valor']
            
            ##atualizando arquivo pessoal##
            with open( key + ".json", "w") as arquivo:
                json.dump(cliente, arquivo, indent = 4)
            
        ##atualizando arquivo geral##
        with open("clientes.json", "w") as arquivo:
            json.dump(clientsList, arquivo, indent = 4)
            
    def atualizaCpf(self, cpf_cnpj):

        ##criando arquivo clienteAtual##
        if os.path.isfile("clienteAtual.json"):
            with open("clienteAtual.json", "r") as arquivo:
                dados = json.load(arquivo)
        else:
            dados = []
 
        ##convertendo dados e atualizando arquivo##
        dados = ClienteAtual(cpf_cnpj)
        dadosConvert = vars(dados)

        with open("clienteAtual.json", "w") as arquivo:
            json.dump(dadosConvert, arquivo, indent = 4)

    def checaCpf(self):

        ##carregando aruivo e armazenando##
        with open("clienteAtual.json", "r") as arquivo:
            dados = json.load(arquivo)

        cpf_cnpj = dados['cpf_cnpj']
        
        return cpf_cnpj
    
    def pedidosDeCredito(self):

        with open("pedidosDeCredito.json", "r") as arquivo:
            pedidos = json.load(arquivo)

        pedidosList = json.dumps(pedidos, indent = 4)

        return(pedidosList)

    def saldo(self, key):

        with open(key + ".json", "r") as arquivo:
            cliente = json.load(arquivo)

        return cliente['saldo']
    
    def trocaSenha(self, key, novaSenha):

        with open("senhas.json", "r") as arquivo:
            senhas = json.load(arquivo)
        
        ##busca cpf e atualiza arquivo##
        for dados in senhas:
            if dados['cpf_cnpj'] == key:
                dados['senha'] = novaSenha

        with open("senhas.json", "w") as arquivo:
            json.dump(senhas, arquivo, indent = 4)

    def verificarCredito(self, key):
        with open("pedidosDeCredito.json", "r") as arquivo:
            pedidosList = json.load(arquivo)
        
        ##busca cpf e retorna o valor, se não retorna 0###
        for pedidos in pedidosList:
            if pedidos['cpf_cnpj'] == key:
                pedido = pedidos['pedidoDeCredito']
                pedidosList.remove(pedidos)

                return pedido

        with open ("pedidosDeCredito.json", 'w') as arquivo:
            json.dump(pedidosList, arquivo, indent = 4)
            
        return 0
