from src.cli.menu import menu
from src.models.cliente import PessoaFisica
from src.models.conta import ContaCorrente
from src.utils.helpers import input_obrigatorio, validar_cpf, validar_data
from src.transacoes.deposito import Depositar
from src.transacoes.saque import Sacar
from src.utils.helpers import validar_cpf

def criar_usuario(clientes):
    while True:
        cpf_input = input_obrigatorio("CPF: ")
        cpf = validar_cpf(cpf_input)

        if cpf:
            break

    # verificar duplicado
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("Usuário já existe!")
            return

    nome = input_obrigatorio("Nome: ")

    while True:
        data_input = input_obrigatorio("Data de nascimento: ")
        data_nascimento = validar_data(data_input)

        if data_nascimento:
            break

    endereco = input_obrigatorio("Endereço: ")

    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)

    print("Usuário criado com sucesso!")

def criar_conta(clientes, contas):
    cpf = input("CPF do cliente: ").strip()

    cliente_encontrado = None

    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return

    numero_conta = len(contas) + 1

    conta = ContaCorrente(numero_conta, cliente_encontrado)

    cliente_encontrado.adicionar_conta(conta)
    contas.append(conta)

    print("Conta criada com sucesso!")

def depositar(clientes):
    cpf = input("CPF: ").strip()

    cliente_encontrado = None

    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return

    if not cliente_encontrado.contas:
        print("Cliente não possui conta!")
        return

    valor = float(input("Valor do depósito: "))

    # try:
    #     valor = float(input("Valor do depósito: "))
    # except ValueError:
    #     print("Valor inválido!")
    # return  

    conta = cliente_encontrado.contas[0]

    transacao = Depositar(valor)    

    cliente_encontrado.realizar_transacao(conta, transacao)

    print("Depósito realizado com sucesso!")

def sacar(clientes):
    cpf_input = input("CPF: ").strip()
    cpf = validar_cpf(cpf_input)

    if not cpf:
        print("CPF inválido!")
        return

    cliente_encontrado = None

    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Cliente não encontrado!")
        return

    if not cliente_encontrado.contas:
        print("Cliente não possui conta!")
        return

    try:
        valor = float(input("Valor do saque: "))
    except ValueError:
        print("Valor inválido!")
        return

    conta = cliente_encontrado.contas[0]

    transacao = Sacar(valor)

    try:
        cliente_encontrado.realizar_transacao(conta, transacao)
        print("Saque realizado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def exibir_extrato(clientes):
    from src.utils.helpers import validar_cpf

    cpf = validar_cpf(input("CPF: "))
    if not cpf:
        return

    cliente = None
    for c in clientes:
        if c.cpf == cpf:
            cliente = c
            break

    if not cliente:
        print("Cliente não encontrado!")
        return

    if not cliente.contas:
        print("Cliente não possui conta!")
        return

    conta = cliente.contas[0]

    conta.exibir_extrato()

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            criar_usuario(clientes)

        elif opcao == "nc":
            criar_conta(clientes, contas)
        
        elif opcao == "d":
            depositar(clientes)
        
        elif opcao == "s":
            sacar(clientes)
        
        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

