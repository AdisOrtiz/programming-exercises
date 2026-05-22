#Importar modulo y cambiar el nombre del modulo con 'as'
#import modulo_saludar as m_saludar

from modulo_saludar import saludar, saludar_perro as s_perro

#Creamos las variables con los saludos
#Forma 1 de llamar al modulo importado con import
#saludar = m_saludar.saludar('Adis')

#Forma 2 de llamar a la función importada del modulo desde from
saludar = saludar('Adis')
#Forma 2 de llamar a la función importada del modulo desde from
saludar_perro = s_perro

#Para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#Accedemos al nombre del modulo
print(f'-------------------\n{__name__}')

#Accedemos al nombre del modulo llamado
#print(f'-------------------\n{m_saludar.__name__}')