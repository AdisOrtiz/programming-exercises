def sumar():
    #Iniciando un bucle
    while True:
        #pidiendo números
        a = input("Número 1: ")
        b = input("Número 2: ")
        #intentando convertir a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanza una excepción, pedir que reingrese los datos
        except Exception as e:
            print("Ingresa un número")
            print(f"ERROR: {e}")
        #si todo salió bien terminamos el bucle
        else:
            break
        finally:
            print("Manejo de excepción finalizado")
    #Muestra el resultado
    return resultado
    
print(sumar())