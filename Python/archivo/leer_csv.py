# import csv
# with open("Python/Archivo/leer.csv") as archivo:
#     leer = csv.reader(archivo)
    
#     for row in leer:
#         print(row)

import pandas as pd

#Usando la función read_csv para leer el archivo csv
df = pd.read_csv("Python/Archivo/leer.csv")
df2 = pd.read_csv("Python/Archivo/leer.csv")

#Obteniendo los datos de la columna nombre
nombres = df["nombre"]

#Ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#Ordenando de forma descendente
df_orden_desendente = df.sort_values("edad",ascending=False)

#Concatenando 2 dataframes
df_concatenado = pd.concat([df,df2])

#Accediendo a las primeras 3 filas con head()
df_filas = df.head(3)

#Accediendo a las últimas 3 filas con tail()
df_filas_ultimas = df.tail(3)

#Accediento a la cantidad de columnas y filas con shape
df_c_f = df.shape

#Accediendo a la edad de la fila 3 con iloc. EL primer parametro es la fila, el 2do la columna
elemento_especifico_iloc = df.iloc[3,2]

#Accediendo a la edad de la fila 2 con iloc. EL primer parametro es la fila, el 2do la columna
elemento_especifico_loc = df.loc[2,"edad"] # Si se reemplaza el 1er parametro por : , se mostraría toda la columna especificada en el 2do parametro

#Accediendo a todas las filas de una columna. 2do parametro es la columna que quiero que se muestre
ape = df.iloc[:,2]

#Devuelve todos los datos de la fila 2
ape1 = df.loc[2,:]

print(f'--------------------\n{ape1}')
