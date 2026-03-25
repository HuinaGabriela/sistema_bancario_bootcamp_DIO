# abstraclassmethod - abstractproperty - antigo e estou usamdo o python 3.12.3 então usarei 

# from abc import ABC, abstractmethod
# from datetime import datetime
# import textwrap


# class Cliente:
#     """
#     Representa um cliente do banco.
#     Pode possuir múltiplas contas.
#     """
#     def __init__(self, endereco):
#         self.endereco = endereco
#         self.contas = []
    
#     def realizar_transacao(self, conta, transacao):
#         """
#         POLIMOSRFISMO - O método realizar_transacao pode aceitar diferentes tipos de transações (Sacar, Depositar) e executá-las sem precisar saber os detalhes de cada tipo. Isso torna o código mais flexível e fácil de manter.
#         """
#         transacao.realizar_transacao(conta)
    
#     def adicionar_conta(self, conta):
#         self.contas.append(conta)
    

# class PessoaFisica(Cliente):
#     """
#     Representa um cliente pessoa física.
#     PessoaFisica herda de Cliente, reutilizando atributos e métodos.
#     Responsabilidade:
#     - Armazenar dados pessoais.
#     """
#     def __init__(self, nome, cpf, data_nascimento, endereco):
#         """
#         Super() - função que chama o método da classe pai (Cliente):
#         Isso evita duplicação de código.
#         Adicionado atributos específicos da classe filha.
#         """
#         super().__init__(endereco)
#         self.nome = nome
#         self.cpf = cpf
#         self.data_nascimento = data_nascimento


# class Historico:
#     """
#     Armazena o histórico de transações de uma conta.
#     Separação de responsabilidades:
#     A conta não gerencia diretamente a lista,
#     delega isso ao Historico.
#     """
#     def __init__(self):
#         self.transacoes = []

#     def registrar_transacao(self, tipo, valor):
#         """
#         Cria um registro padronizado de transação.
#         """
#         transacao = {
#             'tipo': tipo,
#             'valor': valor,
#             'data': datetime.now()
#         }
#         self.transacoes.append(transacao)

#     def exibir_historico(self):
#         """
#         Exibe todas as transações no console.
#         """
#         for transacao in self.transacoes:
#             print(f"{transacao['data']}: {transacao['tipo']} de R${transacao['valor']:.2f}")


# class Conta(ABC):
#     """
#     Classe abstrata que representa uma conta bancária.
#     Não pode ser instanciada diretamente.
#     """
#     def __init__(self, numero_conta, titular, saldo_inicial=0):
#         self.numero_conta = numero_conta
#         self.titular = titular
#         self.saldo = saldo_inicial
#         self.historico = Historico()

#     @abstractmethod
#     def depositar(self, valor):
#         pass

#     @abstractmethod
#     def sacar(self, valor):
#         pass

#     def consultar_saldo(self):
#         """
#         Retorna o saldo atual da conta.
#         """
#         return self.saldo

#     def registrar_transacao(self, tipo, valor):
#         """
#         Encapsula o acesso ao histórico.
#         Evita manipulação direta do histórico fora da classe.
#         """
#         self.historico.registrar_transacao(tipo, valor)


# class ContaCorrente(Conta):
#     """
#     ContaCorrente herda de Conta, implementando os métodos abstratos.
#     """

#     def depositar(self, valor):
#         if valor > 0:
#             self.saldo += valor
#             self.registrar_transacao('Depósito', valor)
#         else:
#             raise ValueError("Valor de depósito deve ser positivo.")

#     def sacar(self, valor):
#         if valor > 0 and valor <= self.saldo:
#             self.saldo -= valor
#             self.registrar_transacao('Saque', valor)
#         else:
#             raise ValueError("Valor de saque inválido ou saldo insuficiente.")


# class Transacao(ABC):
#     """
#     CLASSE ABSTRATA - Transacao é uma classe abstrata que define a estrutura para transações financeiras.
#     Representa uma operação financeira genérica.

#     Permite adicionar novas transações facilmente
#     (ex: Transferência, Pix, etc.)
#     """

#     @abstractmethod
#     def realizar_transacao(self, conta):
#         pass

#     def registrar(self, conta, tipo, valor):
#         """
#         Registra a transação no histórico da conta.
#         """
#         conta.historico.registrar_transacao(tipo, valor)


# class Sacar(Transacao):
#     """
#     Sacar herda de Transacao, implementando o método abstrato.
#     Representa uma operação de saque.
    
#     """
#     def __init__(self, valor):
#         self.valor = valor

#     def realizar_transacao(self, conta):
#         """
#         O método realizar_transacao é implementado de forma diferente para cada tipo de transação (Sacar, Depositar), mas a interface permanece a mesma. Isso permite que o cliente execute transações sem se preocupar com os detalhes de cada tipo.    
#         Implementa a lógica de saque, verificando se o valor é válido e se há saldo suficiente antes de realizar a transação.
#         """
#         if self.valor <= 0:
#             raise ValueError("Valor inválido")

#         if self.valor > conta.saldo:
#             raise ValueError("Saldo insuficiente")

#         conta.saldo -= self.valor
#         self.registrar(conta, 'Saque', self.valor)


# class Depositar(Transacao):
#     """
#     Representa uma operação de depósito herda de de transação e reutiliza o método
#     'registrar' definido na classe base.
#     """
#     def __init__(self, valor):
#         self.valor = valor

#     def realizar_transacao(self, conta):

#         if self.valor <= 0:
#             raise ValueError("Valor de depósito deve ser positivo.")

#         conta.saldo += self.valor
#         self.registrar(conta, 'Depósito', self.valor)
