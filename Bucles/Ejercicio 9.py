#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = 'contraseña'
enter_password = input('Please enter your password: ')
while enter_password != password:
    print('Error -> Please enter the correct password')
    enter_password = input('Please enter your password: ')
    if enter_password== password:
        print('Correct password -> Welcome!')
        break


