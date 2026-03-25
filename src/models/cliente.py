

class Cliente:
    """
    Representa um cliente do banco.
    Pode possuir múltiplas contas.
    """
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        """
        Executa uma transação na conta (polimorfismo)saque ou deposito.
        """
        transacao.realizar_transacao(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Representa um cliente pessoa física.
    Armazena dados pessoais e herda comportamento de Cliente.
    """
    def __init__(self, nome, cpf, data_nascimento, endereco):
        """
        Inicializa os dados do cliente e reutiliza o construtor da classe base.
        """
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
