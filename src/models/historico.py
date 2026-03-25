from datetime import datetime

class Historico:
    """
    Responsável por armazenar e gerenciar o histórico de transações.
    """
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, tipo, valor):
        """
        Registra uma nova transação no histórico.
        """
        transacao = {
            'tipo': tipo,
            'valor': valor,
            'data': datetime.now()
        }
        self.transacoes.append(transacao)

    def exibir_historico(self):
        """
        Exibe todas as transações no console.
        """
        if not self.transacoes:
            print("Nenhuma movimentação.")
            return

        for transacao in self.transacoes:
            data_formatada = transacao['data'].strftime("%d/%m/%Y %H:%M")
            print(f"{data_formatada} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
