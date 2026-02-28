numeros = [1,2,3,4,5,6,7,8,9,0]

#FUnción lambda -> multiplicar por 2
multiplicar_por_dos = lambda x : x*2

#Función que diga si un número es par o no
# def es_par(num):
#     if(num%2==0):
#         return True
    
# #Usando filter con una función común
# numeros_pares = filter(es_par,numeros)

#Creando lo mismo qe antes pero con lambda
numeros_pares = filter(lambda num : num%2 == 0, numeros)
print(numeros_pares)