import csv
path_arquivo = "vendas.csv"

def leitor_csv(nome_do_arquivo_csv:str)->list[dict]:
    """"
    Função que vai ler os dados de um arquivo csv e retorna uma
    lista de dict.

    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos(lista:list[dict])->list[dict]:
    """"
    Função que vai filtrar os produtos que já foram entregues (TRUE).

    """
    lista_produtos_entregues = []
    for produto in lista:
        if produto.get("status") == "true":
            lista_produtos_entregues.append(produto)
    return lista_produtos_entregues


def soma_produtos_entregue(lista_produtos_entregues:list[dict])->float:
    """"
    Função que vai somar os valores dos produtos entregues e retornar o valor total.

    """
    valor_total_entregue = 0
    for produto in lista_produtos_entregues:
        valor_total_entregue += float(produto.get("price"))
    return valor_total_entregue

lista_de_produtos = leitor_csv(path_arquivo)
entregues = filtrar_produtos(lista_de_produtos)
soma_valores_produtos_entregues = soma_produtos_entregue(entregues)
print(soma_valores_produtos_entregues)


