nombre = input("Bienvenid@, ingresa tu nombre: ")
puntuacion = float(input(f"{nombre.title()}, por favor ingrese su puntuacion:\n1 0.0 \n2 0.4 \n3 0.6 o mas \n"))
salario = 2400
if puntuacion == 0.0:
    print(f"{nombre.title()} tu nivel es Inaceptable y la cantidad de dinero recibida sera de {2400*float(puntuacion)}")
if puntuacion == 0.4:
    print(f"{nombre.title()} tu nivel es Aceptable y la cantidad de dinero recibida sera de {2400*float(puntuacion)}")
if puntuacion >= 0.6:
    print(f"{nombre.title()} tu nivel es Meritorio y la cantidad de dinero recibida sera de {2400*float(puntuacion)}")
