from modulos.controler import Controle

# Cria uma instância do Controle
controle = Controle()

# Teste da função addPessoa
controle.addPessoa("João", "123456789", "Rua A", "1234567890", "senha123", "Pessoa Física")

# Teste da função verifCpf
cpf_valido = "123456789"
senha_correta = "senha123"
senha_incorreta = "senha456"

if controle.verifCpf(cpf_valido, senha_correta):
    print("CPF válido e senha correta")
else:
    print("CPF inválido ou senha incorreta")

if controle.verifCpf(cpf_valido, senha_incorreta):
    print("CPF válido e senha incorreta")
else:
    print("CPF inválido ou senha incorreta")

# Teste da função sacar
controle.sacar(100.00, "123456789")

# Teste da função depositar
controle.depositar(200.00, "123456789")

# Teste da função solicitar credito
controle.solCredito(1000000.00, "123456789")

#Teste da função pagamento programado
controle.programarPag(5.00, "31/02", "123456789")

#Teste da função para atualizar pagamento programado
controle.atualizarPagamento("31/02")

# Teste da função rmPessoa
#controle.rmPessoa("123456789")

# Teste da função listar
#controle.listar("123456789")
