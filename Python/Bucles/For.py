lista = ["CRISTO","VIVE","Y","ME","AMA"]
tuplas = (12,23,32,22,93)
conjuntos = {1,2,3,4,5}

#Recorre cada indice de las listas
for l in lista:
    print(l)

#Recorre varias cosas (listas,tuplas,etc) a la vez
for l,t,c in zip(lista,tuplas,conjuntos):
    print(f'Valores de la Lista: {l} - Valores de las tuplas: {t} - Valores de los conjuntos: {c}')
#Respuesta en consola:
#Valores de la Lista: CRISTO - Valores de las tuplas: 12 1
# Valores de la Lista: VIVE - Valores de las tuplas: 23 2
# Valores de la Lista: Y - Valores de las tuplas: 32 3
# Valores de la Lista: ME - Valores de las tuplas: 22 4
# Valores de la Lista: AMA - Valores de las tuplas: 93 5