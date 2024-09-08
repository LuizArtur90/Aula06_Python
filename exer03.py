#Contar Valores Únicos em uma Lista

def valores_unicos(Lista:list[float])-> float:
    return len(set(Lista))

Lista = [10,10,15,15,20,20,35,30]
valores = valores_unicos(Lista)
print(f"A quantidade de valores únicos da lista são {valores} ")