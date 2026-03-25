from abc import ABC, abstractmethod
from src.models.historico import Historico


class Conta(ABC):
    """
    Representa uma conta bancária abstrata.
    """
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = Historico()

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def consultar_saldo(self):
        """
        Retorna o saldo atual da conta.
        """
        return self.saldo

    def registrar_transacao(self, tipo, valor):
        """
        Registra uma transação no histórico da conta.
        """
        self.historico.registrar_transacao(tipo, valor)
    
    def exibir_extrato(self):
        print("\n===== EXTRATO =====")
        self.historico.exibir_historico()
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")


class ContaCorrente(Conta):
    """
    ContaCorrente herda de Conta, implementando os métodos abstratos.
    """

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao('Depósito', valor)
        else:
            raise ValueError("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.registrar_transacao('Saque', valor)
        else:
            raise ValueError("Valor de saque inválido ou saldo insuficiente.")
