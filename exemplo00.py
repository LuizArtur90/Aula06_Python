from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

valores = [10,15,20]
resultado = calcular_media(valores)

print(f"A média dos valores é: {resultado}")