from etl import leitor_csv, filtrar_produtos , soma_produtos_entregue

path_arquivo = "vendas.csv"


lista_de_produtos = leitor_csv(path_arquivo)
entregues = filtrar_produtos(lista_de_produtos)
soma_valores_produtos_entregues = soma_produtos_entregue(entregues)
print(soma_valores_produtos_entregues)