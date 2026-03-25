# executar testes funcional e coverage:
# pytest

# pytest --cov=src --cov-report=html --cov-report=term-missing
# htmlcov/index.html

# comandos uteis caso não atualize o coverage: 
# coverage erase - apaga os dados de cobertura
# pytest --cov=src --cov-report=html --cov-append=0


import pytest
from src.models.conta import ContaCorrente
from src.transacoes.deposito import Depositar
from src.transacoes.saque import Sacar
from src.models.cliente import PessoaFisica


@pytest.fixture
def cliente_com_conta():
    cliente = PessoaFisica("João", "12345678900", "01/01/1990", "Rua A")
    conta = ContaCorrente("001", cliente, 100)
    cliente.adicionar_conta(conta)
    return cliente, conta


def test_deposito_valido(cliente_com_conta):
    cliente, conta = cliente_com_conta

    cliente.realizar_transacao(conta, Depositar(50))

    assert conta.saldo == 150
    assert len(conta.historico.transacoes) == 1


def test_deposito_valor_invalido(cliente_com_conta):
    cliente, conta = cliente_com_conta

    with pytest.raises(ValueError):
        cliente.realizar_transacao(conta, Depositar(-10))


def test_saque_valido(cliente_com_conta):
    cliente, conta = cliente_com_conta

    cliente.realizar_transacao(conta, Sacar(50))

    assert conta.saldo == 50


def test_saque_sem_saldo(cliente_com_conta):
    cliente, conta = cliente_com_conta

    with pytest.raises(ValueError):
        cliente.realizar_transacao(conta, Sacar(200))


def test_historico_registrado(cliente_com_conta):
    cliente, conta = cliente_com_conta

    cliente.realizar_transacao(conta, Depositar(100))
    cliente.realizar_transacao(conta, Sacar(50))

    historico = conta.historico.transacoes

    assert len(historico) == 2
    assert historico[0]["tipo"] == "Depósito"
    assert historico[1]["tipo"] == "Saque"


def test_consultar_saldo(cliente_com_conta):
    _, conta = cliente_com_conta

    assert conta.consultar_saldo() == 100


def test_pessoa_fisica():
    cliente = PessoaFisica("Maria", "123", "01/01/1990", "Rua B")

    assert cliente.nome == "Maria"
    assert cliente.cpf == "123"
    assert cliente.endereco == "Rua B"