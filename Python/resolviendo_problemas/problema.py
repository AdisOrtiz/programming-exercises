#2 listas, una con nombres otra con apellidos
nombres = ["JuanC","Mere","Adriana","Andrea"]
apellidos = ["Ortiz","Gomez","Ortiz1","Ortiz2"]

#Registrar/ingresar esta información en un TXT de forma optima

with open("texto_nombre_apellidos.txt","a") as archivo:
    archivo.writelines("Los datos son: \n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]