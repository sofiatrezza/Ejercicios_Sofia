nombre = input("Bienvenid@, ingresa tu nombre: ")
renta = int(input("Por favor ingrese su renta anual en €: "))
if renta < 10000:
    print(f"{nombre.title()} tu tipo de impositivo es del 5%")
if renta >= 10000 and renta <= 20000:
    print(f"{nombre.title()} tu tipo de impositivo es del 15%")
if renta >= 20000 and renta <= 35000:
    print(f"{nombre.title()} tu tipo de impositivo es del 20%")
if renta >= 35000 and renta <= 60000:
    print(f"{nombre.title()} tu tipo de impositivo es del 30%")
if renta > 60000:
    print(f"{nombre.title()} tu tipo de impositivo es del 45%")