#Opción 1 de leer un archivo .txt
#Usando open para abrir un archivo con una codificación universal (UTF-8)
#archivo = open("Python/Archivo/texto.txt",encoding="UTF-8")

#Leer un archivo completo
#archivo = archivo.read()

#Leer linea por linea
#lineas = archivo.readline()

#Cerrar el archivo
#archivo.close()
#print(archivo)

#--------------------------
# Opción 2 - Optimo
with open("Python/Archivo/texto.txt",encoding="UTF-8") as archivo:
    #Leemos y mostramos el archivo
    print(archivo.read())

#No es necesario cerrarlo al usar with
 