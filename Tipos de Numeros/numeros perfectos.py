"""Número perfecto: todo número natural que es igual a la suma de sus divisores 
propios (es decir, todos sus divisores excepto el propio número). Por ejemplo, 
6 es un número perfecto ya que sus divisores propios son 1, 2, y 3 y se cumple que 
1+2+3=6. Los números 28, 496 y 8128 también son perfectos."""

n = input('Ingrese un numero: ')
n = int(n) #validando que es un numero
N = n

divisores = []


for i in range(1 , int(n/2)+1):
    if n%i == 0:
        divisores.append(i)
        print(divisores)

sum_divisores = sum(divisores)
print(sum_divisores)
if sum_divisores == N:
    print(f'El numero {N} es un numero perfecto')
elif sum_divisores != N:
    print(f'El numero {N} NO es un numero perfecto')
else:
    print('error')

"""suma = 0

for j in divisores:
    suma += j

print(suma)"""

'''if suma == N:
    print(f'El numero {N} es un numero perfecto')
else:
    print(f'El numero {N} NO es un numero perfecto')'''



