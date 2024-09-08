def filtrar_acima_limite(dados:list[float], limite:float)->float:
    """
    Filtra os elementos de uma lista que estão acima de um determinado limite.

    Parâmetros:
    dados (list): Lista de valores numéricos.
    limite (float): O valor limite.

    Retorna:
    resultado: Uma nova lista com os valores maiores que o limite.
    """
    return [valor for valor in dados if valor > limite]

# Exemplo de uso:
dados = [10, 20, 30, 40, 50, 60]
limite = 30
resultado = filtrar_acima_limite(dados, limite)
print(f"O resultado da lista filtrada pelo limite {limite} é: {resultado}")