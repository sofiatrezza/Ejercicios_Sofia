#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
# posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre 
# y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input('Bienvenid@, ingresa tu nombre: ')
sexo = input('¿Cuál es tu sexo; masculino o femenino? ')
if sexo == "femenino":
   if nombre.lower() <  "m":
    print(f"{nombre} tu grupo es el A")
else:
    print(f"{nombre} tu grupo es el B")
if sexo == "masculino":
    if nombre.lower() >  "n":
         print(f"{nombre} tu grupo es el A")
else:
    print(f"{nombre} tu grupo es el B")