#Calcular Média de Valores em uma Lista

def Calcular_media(valores:list[float])->float:
    return sum(valores)/len(valores)

valores = [10,15,20]
resultado = Calcular_media(valores)

print(f"O valor da média é: {resultado}")



