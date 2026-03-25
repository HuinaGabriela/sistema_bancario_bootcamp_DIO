from src.transacoes.transacao import Transacao


class Depositar(Transacao):
    """
    Representa uma operação de depósito herda de transação e reutiliza o método
    'registrar' definido na classe base.
    """
    def __init__(self, valor):
        self.valor = valor

    def realizar_transacao(self, conta):

        if self.valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo.")

        conta.saldo += self.valor
        self.registrar(conta, 'Depósito', self.valor)