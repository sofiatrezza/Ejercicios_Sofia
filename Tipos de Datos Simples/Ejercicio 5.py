# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

hours_worked = int(input("Please enter how many hours do you work per day: "))
price_per_hour = int(input("Enter the price of your hour: "))
salary = hours_worked*price_per_hour
print(f"Your salary is {salary} per day")
