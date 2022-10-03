#•	Registrar y cobrar al paciente: debe solicitarse nombre, apellido y cédula del paciente, y el 
# id de la patología que padece. Esta información debe almacenarse en la estructura de datos de su preferencia.
#  Debe mostrarse en pantalla la factura generada, con los datos del paciente, la patología que padece y el monto 
# a pagar.
# Ver pacientes: debe preguntarse por la patología a consultar y mostrar los pacientes registrados en el sistema 
# que la padezcan.
# Menú principal que permita seleccionar la acción que se quiera realizar.
# Debe volverse al menú principal cada vez que se termine alguna operación (es decir, el código debe seguir 
# ejecutándose hasta que el usuario decida salir).
# Los mensajes por consola deben verse ordenados y ser intuitivos.

pathologies = {"Respiratory system": [{"id": 1, "name": "Cystic Fibrosis","price": 300}, {"id": 2, "name": "Emphysema", "price": 500}, {"id": 3,"name": "Tuberculosis","price": 450}], 
"Nervous system": [{"id": 4,"name": "Parkinson","price": 800},{"id": 5,"name": "Epilepsy","price": 600}],
"Endocrine system":[{"id": 6,"name": "Diabetes","price": 350 },{"id": 7,"name": "Acromegaly","price": 700},{"id": 8,"name": "Hashimoto’s thyroiditis","price": 900}]}


data_respiratory = []
data_nervous = []
data_endocrine = []
while True:
    print(f"Welcome to Mercy Hospital, please enter your information and ID pathology. \n ->Follow the steps:")
    patient_info = input('Enter your full name: ')
    id_info = input('Enter your ID number: ')
    pathology_info  = input(f"Enter your type of pathology: \na Respiratory system \nb Nervous system \nc Endocrine system \n ")
    if pathology_info == "a":
        respiratory= input(f"We have the following services: \n1 Cystic Fibrosis \n2 Emphysema \n3 Tuberculosis \n ")
        data_respiratory.extend([patient_info.title(), id_info, pathology_info, respiratory])
        if respiratory == "1":
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_respiratory[0: 2]}")
            print({pathologies["Respiratory system"][0]})
        elif respiratory == "2":
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_respiratory[0: 2]}")
            print(pathologies["Respiratory system"][1])
        else:
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_respiratory[0: 2]}")
            print(pathologies["Respiratory system"][2])
       
    elif pathology_info == "b":
        nervous = input("We have the following services: \n4 Parkinson \n5 Epilepsy \n")
        data_nervous.extend([patient_info.title(), id_info, pathology_info, nervous])
        if nervous == "4":
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_nervous[0: 2]}")
            print(pathologies["Nervous system"][0])
        else:
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_nervous[0: 2]}")
            print(pathologies["Nervous system"][1])

    elif pathology_info == "c":
        endocrine = input("We have the following services: \n6 Diabetes \n7 Acromegaly \n8 Hashimoto’s thyroiditis \n")    
        data_endocrine.extend([patient_info.title(), id_info, pathology_info, endocrine])
        if endocrine == "6":
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_endocrine[0: 2]}")
            print(pathologies["Endocrine system"][0])
        elif endocrine == "7":
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_endocrine[0: 2]}")
            print(pathologies["Endocrine system"][1])
        else:
            receipt = print(f"You have been registered! \n Thanks for your patient, here is your receipt: \n {data_endocrine[0: 2]}")
            print(pathologies["Endocrine system"][2])
       

    if input("Do you want to exit?: \nY- Yes \nN - No \n")== "Y":
        break