'''Diseñe un algoritmo que genere el siguiente recorrido en una matriz cuadrada:
1           9
2  15    8  10
3     7     11
4  6    14  12
5           13
'''
#Pedir el número para el tamaño de la matriz
tamano_matriz = int(input('Ingrese un número para el tamaño de la matriz: '))
matriz = []
num = 1
col = 1

#Llenado de la matriz
for i in range(tamano_matriz):
    lista = ['']*tamano_matriz
    matriz.append(lista)

#Llenando primera columna
for i in range(tamano_matriz):
    matriz[i][0] = num
    num+=1

#Llenando la matriz desde la diagonal inferior izquierda a la derecha 
for i in range(tamano_matriz-2,-1,-1):
    matriz[i][col] = num
    num += 1
    col += 1

#Llenando la última columna
for i in range(1,tamano_matriz):
    matriz[i][tamano_matriz-1] = num
    num += 1

col = tamano_matriz-2
#Llenando matriz desde la diagonal inferior derecha a la izquierda
for i in range(tamano_matriz-2,-1,-1):
    if matriz[i][col] == '':
        matriz[i][col] = num
        num += 1
    col -= 1

for i in matriz:
    for j in i:
        print(f'{j:5}', end="")
    print('')