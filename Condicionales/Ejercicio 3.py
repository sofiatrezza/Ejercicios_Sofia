#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

dividendo = float(input("Ingrese un numero: "))
divisor = float(input("Ingrese otro numero: "))
if divisor ==  0:
    print("Error, no existe la division entre cero.")
else:
    print(dividendo/divisor)