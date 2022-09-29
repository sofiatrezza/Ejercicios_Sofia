#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
# ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario 
# tiene que tributar o no.

nombre = input("Bienvenido, ingresa tu nombre: ")
edad = input(f"{nombre.title()}, ingresa tu edad: ")
ingresos = int(input(f"Tus ingresos mensuales son: "))
if edad > 16 and ingresos >= 1000:
    print(f"{nombre}, debes tributar tus impuestos")
else:
    print("No debes tributar")
