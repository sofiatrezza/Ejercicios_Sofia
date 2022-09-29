#Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# si es mayor de edad o no.

age = int(input("Please enter your age: "))
if age >= 18:
    print(f"You are underage")
else:
    print(f"You are an adult")