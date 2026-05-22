'''
🌀 Nuevo ejercicio

Diseña un algoritmo que genere una matriz n×n con números consecutivos en espiral desde la esquina superior izquierda 
hacia adentro.

Ejemplo con n = 5:

1   2   3   4   5
16 17  18  19  6
15 24  25  20  7
14 23  22  21  8
13 12  11  10  9
'''

#Pedir número del tamaño de la matriz
tam_matriz = int(input('Ingrese un número: '))
matriz = []
num = 1 # Número consecutivo
#Difinición de limites
top = 0 #limite superior -> fila inicial
bottom = tam_matriz-1 # última fila
left = 0 #Primera columna disponible
right = tam_matriz-1 #última columna disponible

#Llenado de la matriz con 0
for i in range(tam_matriz):
    lista = [0]*tam_matriz
    matriz.append(lista)

while(top <= bottom and left <= right):

    #Llenando la primera fila ->
    for i in range(left,right+1):
        matriz[top][i] = num
        num+=1
    top += 1 # Se suma 1 para que la fila vaya bajando

    #Llenando la última columna de arriba-abajo
    for i in range(top, bottom+1):
        matriz[i][right] = num
        num+=1
    right -= 1 # Se resta 1 para que ya no sea la última columna sino una antes
    
    if top <= bottom: # Verifica si todavía existen filas antes de moverse
        #Llenando la última fila de derecha a izquierda <-
        for i in range(right,left-1,-1):
            matriz[bottom][i] = num
            num+=1
        bottom -= 1 #Se resta 1 para que ya no sea la última fila sino la ante penultima

    if left <= right: # Verifica si todavía existen columnas antes de moverse
        #Llenando la primera columna de abajo-arriba
        for i in range(bottom,top-1,-1):
            matriz[i][left] = num
            num+=1
        left += 1
    
for i in matriz:
    for j in i:
        print(f'{j:4}', end="")
    print('')