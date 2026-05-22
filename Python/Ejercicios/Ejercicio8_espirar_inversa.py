# espiral desde el centro hacia afuera 🌀
# Ejemplo n = 5:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

def espiral_centro(tamano):
    matriz = []
    
    #Llenando la matriz con 0
    for i in range(tamano):
        lista = [0]*tamano
        matriz.append(lista)
    
    #Encuentro la mitad de la matriz y tomo la parte entera
    mitad = tamano//2
    fila = mitad
    columna = mitad
    matriz[mitad][mitad] = 1
    num = 2
    direcciones = [
        (0, 1),   #→ derecha
        (1, 0),   #↓ abajo
        (0, -1),  #← izquierda
        (-1, 0)  #↑ arriba
    ]
    dir_actual = 0 #Empezamos mirando a la derecha
    longitud_paso = 1 #Variable que hace crecer la espiral
   
    
    while num <= tamano*tamano:
        #Repetir 2 veces
        for i in range(2):
            for paso in range(longitud_paso):
                fila += direcciones[dir_actual][0]
                columna += direcciones[dir_actual][1]
                #si estoy dentro de la matriz
                if 0 <= fila < tamano and 0 <= columna < tamano:
                    matriz[fila][columna] = num
                    num += 1
            dir_actual = (dir_actual + 1) % 4
        longitud_paso += 1
                
    
    #Muestro la matriz con espacio
    for i in matriz:
        for j in i:
            print(f'{j:4}', end="")
        print('')

espiral_centro(7)
