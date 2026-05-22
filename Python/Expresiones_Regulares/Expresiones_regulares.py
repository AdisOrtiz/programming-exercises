import re #Importa Expresiones Regulares

texto = '''Hola, esta es la cadena 1.., ¿cómo les va¨?
Esta es la linea 2. del texto.
Esta es la linea 3 del texto'''

#Haciendo una busqueda simple
#resultado = re.findall("Esta",texto)

#\d -> busca digitos numéricos del 0 - 9
#resultado = re.findall(r"\d", texto)

#\D -> busca TODO menos digitos numéricos del 0 - 9
#resultado = re.findall(r"\D", texto)

#\w -> busca caracteres alfanuméricos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w", texto)

#\W -> busca TODO menos caracteres alfanuméricos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W", texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s", texto)

#\S -> busca TODO espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\S", texto)

#\n -> busca saltos de linea
#resultado = re.findall(r"\s", texto)

#. -> busca TODO menos saltos de linea
#resultado = re.findall(r"\S", texto)

#\ -> cancela caracteres especiales, cancelando la función del punto y buscando puntos
resultado = re.findall(r"\.",texto)

#armando una cadena que busque un número, seguido de un puntoy un espacio
resultado = re.findall(r"\d\.\s",texto)

print(resultado)