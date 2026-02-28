# 1 Alumno es profesor y otro alumno es aistente
# A) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
# B) El mayor es el profesor y el menor es el asistente

#OPCIÓN 1
# edad_alumnos = list([14,15,13,15,16,18,12])

# #A) Ordenar los datos de menor a mayor
# edad_alumnos.sort()

# #B) Alumno mayor
# alumno_mayor = max(edad_alumnos)
# alumno_menor = min(edad_alumnos)

# #Resultado
# print(f'Orden de edad de alumnos de menor a mayor: {edad_alumnos}.\n El alumno mayor tiene {alumno_mayor} años, por lo tanto es el profesor. \n El alumno menor tiene {alumno_menor} años, por lo tanto es el asistente')

#OPCIÓN 2
#Cantidad de estudiantes

#Nombre y edad de los estudiantes
def estudiantes(cant_est):
    total_estudiantes = []
    for e in range(cant_est):
        e+=1
        nombre = input(f"Ingresa el nombre del estudiante {e}: ")
        edad = int(input(f"Ingresa la edad del estudiante {e}: "))
        estudiante = (nombre, edad)
        #A la lista del total de estudiante se le va agregando la tupla de estudiante(el nombre y la edad)
        total_estudiantes.append(estudiante)
    
    #A) Ordenar los datos de menor a mayor
    total_estudiantes.sort(key=lambda x:x[1])
    #Obtener el estudiante de mayor edad
    tupla_mayor_edad = total_estudiantes[-1]
    #Obtener el estudiante de menor edad
    tupla_menor_edad = total_estudiantes[0]
    
    return total_estudiantes,tupla_mayor_edad,tupla_menor_edad #estudiante_mayor_edad,estudiante_menor_edad

cant_est = int(input("Ingrese cuantos estudiantes hay: "))
orden_estud,estud_may, estud_men = estudiantes(cant_est)

print(f'Este es el orden de los estudiantes de menor a mayor edad: {orden_estud}')
print(f'El estudiante de mayor edad es: {estud_may[0]} con {estud_may[1]} años, por lo tanto es el/la profesor/a')
print(f'El estudiante de menor edad es: {estud_men[0]} con {estud_men[1]} años, por lo tanto es el/la asistente')