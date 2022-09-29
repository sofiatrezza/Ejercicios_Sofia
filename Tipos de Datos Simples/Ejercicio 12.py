#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

from functools import total_ordering


precio_barra_pan = 3.49
precio_barra_vieja = round(precio_barra_pan - precio_barra_pan*0.60, 3)
barras_vendidas = int(input(f"Ingrese la cantidad de barras de pan vendidas que no son del día: "))
print(f"El precio de una barra de pan del día es de {precio_barra_pan}, si no es  del día se le hace un descuento de {precio_barra_vieja}")
total = round(int(barras_vendidas)*float(precio_barra_vieja), 3)
print(f"El precio total obtenido por las barras del pan que no son del día es de {total}")