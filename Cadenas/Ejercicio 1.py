#Escribir un programa que pregunte el nombre del usuario en la consola y u
# n número entero e imprima por pantalla en líneas distintas el nombre del usuario 
# tantas veces como el número introducido.

name = input(f"Please enter your name: ")
number = int(input(f"Please enter a number:"))
print((name + "\n") * number)