#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
# Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

lista_asignaturas =["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura in lista_asignaturas:
    print(f'Yo estudio {asignatura}')