import re
from datetime import datetime


def input_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Campo obrigatório!")


def validar_cpf(cpf: str) -> str:
    """
    Aceita números e formata para 000.000.000-00
    """
    cpf = re.sub(r"\D", "", cpf)  # remove tudo que não for número

    if len(cpf) != 11:
        print("CPF deve ter 11 dígitos!")
        return None

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def validar_data(data_str: str) -> str:
    formatos = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]

    for formato in formatos:
        try:
            data = datetime.strptime(data_str, formato)

            hoje = datetime.now()

            # não pode ser no futuro
            if data > hoje:
                print("Data não pode ser no futuro!")
                return None

            # idade mínima 18 anos
            idade = hoje.year - data.year

            if idade < 18:
                print("⚠️ Cliente deve ter pelo menos 18 anos!")
                return None

            # evitar datas muito antigas (ex: antes de 1900)
            if data.year < 1900:
                print("Data inválida!")
                return None

            return data.strftime("%d/%m/%Y")

        except ValueError:
            continue

    print("Data inválida! Use formato válido.")
    return None