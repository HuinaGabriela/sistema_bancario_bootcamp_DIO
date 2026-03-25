import textwrap

def menu():
        menu = """\n
        =========== Menu ===========
        [d] \t Depositar
        [s] \t Sacar
        [e] \t Extrato
        [nc] \t Nova Conta
        [lc] \t Listar Contas
        [nu] \t Novo Usuário
        [q] \t Sair
        ============================
        """
        return input(textwrap.dedent(menu))