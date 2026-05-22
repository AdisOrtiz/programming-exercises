#Serie de fibonacci desde X hasta Y
#Opción 1
def fibonacci(num,num2):
    a,b = num,num #Desempaquetamos, es así: a = num y b = num
    for i in range(num,num2):
        c = a + b
        print(f'{a} + {b} = {c}')
        a,b = b,c #Desempaquetamos, es así: a = b y b = c
fibonacci(1,11)

#Opción2
def fibonacci(num,num2):
    a,b = num,num #Desempaquetamos, es así: a = num y b = num
    lista_fibonacci = []
    for i in range(num,num2):
        c = a + b
        lista_fibonacci.append(c)
        a,b = b,c #Desempaquetamos, es así: a = b y b = c
    return lista_fibonacci
f = fibonacci(1,11)
print(f'Lista fibonacci {f}')