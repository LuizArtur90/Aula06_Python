#Converter Celsius para Fahrenheit em uma Lista

def calc_celsius_para_fahrenheit(Lista:list[float])->list[float]:
    return [(9/5) * temp + 32 for temp in Lista ]

Lista = [10,20,35,37,41]
Fahrenheit_lista = calc_celsius_para_fahrenheit(Lista)

print (f"A lista atualizada para Fahrenheit é: {Fahrenheit_lista} ")
