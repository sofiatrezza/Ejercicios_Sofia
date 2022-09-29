#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Por favor ingrese un numero: "))
if numero % 2 ==0:
    print(f"El numero {numero} es par")
else: 
    print(f"El numero {numero} es impar")