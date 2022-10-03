#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
# la muestre por pantalla.

lista_materia = ['Mate', 'Quimica']
while True:
    materia = input('Ingrese la asignatura su curso: ')
    lista_materia.append(materia)
    print(f'La asignatura {materia} fue agregada a la lista!')
    print(lista_materia)
