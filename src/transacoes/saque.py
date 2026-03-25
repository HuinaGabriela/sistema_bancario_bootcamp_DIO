from src.transacoes.transacao import Transacao


class Sacar(Transacao):
    """
    Sacar herda de Transacao, implementando o método abstrato.
    Representa uma operação de saque.
    
    """
    def __init__(self, valor):
        self.valor = valor

    def realizar_transacao(self, conta):
        """
        Executa um saque na conta.
        Verificando se o valor é válido e se há saldo suficiente antes de realizar a transação.
        """
        if self.valor <= 0:
            raise ValueError("Valor inválido")

        if self.valor > conta.saldo:
            raise ValueError("Saldo insuficiente")

        conta.saldo -= self.valor
        self.registrar(conta, 'Saque', self.valor)