#Diseñe un algoritmo que realice la siguiente secuencia de intercambio para una matriz de cuadrada de n dimensión.
'''
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
--------------
5  4  23 2  1
10 9  18 7  6
15 14 13 12 11
20 19 8  17 16
25 24 3  22 21

leer n
crear matriz original de tamaño n x n
crear matriz nueva de tamaño n x n

PARA cada fila i desde 0 hasta n-1
    PARA cada columna j desde 0 hasta n-1
        
        SI j es la columna central (j == n//2)
            nueva[i][j] = original[n-1-i][j]   // espejo vertical
        
        SINO
            nueva[i][j] = original[i][n-1-j]   // espejo horizontal
    
    FIN PARA
FIN PARA

mostrar matriz nueva
'''

#Pedir número del tamaño de la matriz
n = int(input('Ingrese un número para el tamaño de la matriz: '))
original = []
nueva = []
contador = 1

#Llenar matriz original
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(contador)
        contador += 1
    original.append(fila)

#Mostrar matriz original
for i in original:
    print(f'{i}')
    
#Llenar matriz nueva
for i in range(n):
    fila = [0]*n
    nueva.append(fila)
    
#Recorrer la matriz
for i in range(n):
    for j in range(n):
        #Si j es la columna central se invierte la fila
        if j == n//2 and n%2==1:
            print(f'valor de j al recorrer la matriz {j}')
            nueva[i][j] = original[n-1-i][j] #espejo vertical. 
        else:
            nueva[i][j] = original[i][n-1-j] #espejo horizontal

print('\n--------- Matriz Invertida --------\n')
#mostrar matriz nueva
for filas in nueva:
    for num_filas in filas:
        print(f'{num_filas:4}', end="") #imprime este número ocupando 4 espacios. con end="" evita los saltos de linea
    print('')
