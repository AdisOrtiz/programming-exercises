#Crear una función que pida un número y genere los números primos desde el 1 hasta el número ingresado
#Números enteros
#El número 1 no es primo
#Solo tienen dos divisores: el 1 y ellos mismos
#El único número par y primo es el 2

def num_primos(num_ingresado):
    lista_numeros_primos = []
    #Bucle que va desde el 2 hasta X número
    num_ingresado+=1
    for num_ingr in range(2, num_ingresado):
        #Obtengo los números impares
        if(num_ingr>2 and num_ingr%2==0):
            continue
        else:
            #Suposición inicial, todos los números son primos
            es_primo = True
            #Optenemos raíz cuadrada del número actual
            raiz = int(num_ingr ** 0.5)
            raiz1 = raiz + 1
            for valida_num in range(2,raiz1):
                #Dividir número actual hasta la raíz cuadrada
                if(valida_num <= raiz):
                    if(num_ingr%valida_num==0):
                        #No es primo
                        es_primo = False
                        break
        if(es_primo):
            lista_numeros_primos.append(num_ingr)
    return lista_numeros_primos

#Pide un número al usuario mayor a 1
num = int(input("Ingresa un número mayor a 1 para validar que números son primos: "))
while(num <= 1):
    num = int(input("Ingresa un número mayor a 1 para validar que números son primos: "))

lista_primos = num_primos(num)
print(f"Los números primos son: {lista_primos}")