#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input("Please enter a number > 0: "))
for i in range(number, -1, -1):
    print(i, end=",")

