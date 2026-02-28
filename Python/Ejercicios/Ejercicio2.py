#Crear una función que pida un número y genere los números primos desde el 1 hasta el número ingresado
#Números enteros
#El número 1 no es primo
#Solo tienen dos divisores: el 1 y ellos mismos
#El único número par y primo es el 2

def num_primos(num_ingresado):
    lista_numeros_primos = []
    #Bucle que va desde el 2 hasta X número
    for n in range(2, num_ingresado):
        #Suposición inicial, todos los números son primos
        
        print(n)
        # numero_actual = n
        
        # #Por defecto agrega el 2 a la lista de números primos
        # if(n == 2):
        #     lista_numeros_primos.append(n)
        
        # #Validar si el resto de x número es 0 -> no es primo
        # # if (n%2==0 and n>2):
        # #     #No es primo
        # #     continue

        # #Bucle para dividir número actual por otros números menores que él
        # for i in (2, numero_actual):
        #     #Buscamos la raíz cuadrada del número que se está verificando
        #     raiz = numero_actual**2
        #     if(i<raiz):
        #         #Si el resto de la división es 0, no es primo
        #         if (numero_actual%i==0):
        #             print(f"{numero_actual} no es un número primo")
        #         else:
        #             lista_numeros_primos.append(numero_actual)
    # return lista_numeros_primos

# #Pide un número al usuario mayor a 1
# num = int(input("Ingresa un número mayor a 1 para validar que números son primos: "))
# while(num <= 1):
#     num = int(input("Ingresa un número mayor a 1 para validar que números son primos: "))
    
# numeros_primos = num_primos(5)
# print(f"Los números primos del 2 hasta el {num} son: {numeros_primos}")

num_primos(5)
