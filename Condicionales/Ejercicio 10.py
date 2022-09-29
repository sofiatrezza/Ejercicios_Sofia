#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes 
# que lleva.

nombre = input("Bienvenid@ a la pizzería Bella Napoli, ingresa tu nombre: ")
tipo_pizza = input(f"{nombre.title()}, te ofrecemos dos tipos de pizza con base de mozarrella y tomate: \n1 Vegetariana \n2 NoVegetariana \n")
if tipo_pizza == "1":
    ingredientes_v = input(f"{nombre.title()}, te ofrecemos dos toppings: \na Pimiento \nb Tofu \n")
    if ingredientes_v == "a":
        print(f"{nombre.title()}, tu orden es una Pizza Vegetariana con topping de Pimiento")
    else:
        print(f"{nombre.title()}, tu orden es una Pizza Vegetariana con topping de Tofu")

if tipo_pizza == "2":
    ingredientes_nv = input(f"{nombre.title()}, te ofrecemos tres toppings: \nc Pepperoni \nd Jamón \ne Salmón \n")
    if ingredientes_nv == "c":
        print(f"{nombre.title()}, tu orden es una Pizza NoVegetariana con topping de Pepperoni")
    elif ingredientes_nv == "d":
        print(f"{nombre.title()}, tu orden es una Pizza NoVegetariana con topping de Jamón")
    else:
        print(f"{nombre.title()}, tu orden es una Pizza NoVegetariana con topping de Salmón")

print("Gracias por preferirnos, -Bella Napoli")
