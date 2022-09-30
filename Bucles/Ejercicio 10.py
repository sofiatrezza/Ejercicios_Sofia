#Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla si es un número primo o no.

n = int(input('Ingrese un número entero: '))
cont = 0
for i in range(n-1, 1, -1):
    if n % 2 == 0:
        print(f"El número {n} no es primo")
    else:
        print(f"El numero {n} es primo")
        


