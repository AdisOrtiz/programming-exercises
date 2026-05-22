#Crear una calculadora, donde el usuario escoja la operación e ingrese los 2 números para dicha operación
def cal(num1,num2,operador):
    if(operador == '+'):
        suma = num1 + num2
        return suma
    elif(operador == '-'):
        resta = num1 - num2
        return resta
    elif(operador == '*'):
        multip = num1 * num2
        return multip
    elif(operador == '/'):
        divi = num1 / num2
        return divi

num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
operador = input('Ingrese el operador con el que desea que se realice la operación \nSuma: + \nResta: -\nMultiplicación: * \nDivisión: / \n= ')
while(operador != ''):
    if(operador == '+' or operador == '-' or operador == '*' or operador == '/'):
        break
    else:
        operador = input('Ingrese el operador con el que desea que se realice la operación \nSuma: + \nResta: -\nMultiplicación: * \nDivisión: / \n= ')

resultado = cal(num1,num2,operador)
print(f'El resultado de la operación fue: {resultado}')
