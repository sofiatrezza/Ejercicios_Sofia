#Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla si es un número primo o no.

n = int(input('Ingrese un número entero: '))
is_prime = True
for i in range(n-1, 1, -1):
    if n % i == 0:
        is_prime = False
if is_prime:
    print(f"El número {n} es primo")
else:
    print(f"El numero {n} no es primo")