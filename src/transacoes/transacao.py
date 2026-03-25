from abc import ABC, abstractmethod


class Transacao(ABC):
    """
    CLASSE ABSTRATA - Transacao é uma classe abstrata que define a estrutura para transações financeiras.
    Representa uma operação financeira genérica.

    Permite adicionar novas transações facilmente
    (ex: Transferência, Pix, etc.)
    """

    @abstractmethod
    def realizar_transacao(self, conta):
        pass

    def registrar(self, conta, tipo, valor):
        """
        Registra a transação no histórico da conta.
        """
        conta.historico.registrar_transacao(tipo, valor)