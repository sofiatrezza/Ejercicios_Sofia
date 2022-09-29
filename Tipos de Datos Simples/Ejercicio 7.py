#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el 
# índice de masa corporal calculado redondeado con dos decimales.

weight =float(input(f"Please enter your weight in kg: "))
height =float(input(f"Please enter your height in meters: "))
imc = round(weight/(height**2))
print(f"Your IMC is {imc}")
