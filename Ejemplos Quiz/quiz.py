pathologies = {
    "Respiratory system":
    [
        {
            "id": 1,
            "name":"Cystic Fibrosis",
            "price": 300
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system":
    [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system":
    [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700},
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }]}


data_pathology = []
temp_key = [i for i in pathologies]
x = ["id", "name"] # Esto lo puse asi porque por algun motivo no me dejaba escribirlo donde deberia, en donde la x
while True:
    print(f"Welcome to Mercy Hospital, please enter your information and ID pathology. \n ->Follow the steps:")
    patient_info = input('Enter your full name: ')
    id = input('Enter your ID number: ') # Si quieres la palabra info quitala, se sobreentiende que la id del paciente es su id
    print("Enter your type of pathology: ")
    for i in range(0, len(temp_key)):
        print(f">> {i + 1} - {temp_key[i]}.")

    pathology_info  = int(input(" ==> "))
    
    temp_key_b = [i for i in pathologies[temp_key[pathology_info-1]]] # esto de temp_key_b creo se entiende, pero no agarres esta mala maña, trata desde el principio si vas a tener mas de una variable que te sera temporal, tenerlo planeado para poner nombres mas cortos
    print("please, select a pathology: ") # Mi ingles no es lo maximo pero creo se entiende
    ids= [] # Osea, varias id, por eso, id - s
    for j in range(0, len(temp_key_b)):
        ids.append(temp_key_b[j][x[0]])
        print(f"{temp_key_b[j][x[0]]} - {temp_key_b[j][x[1]]}. ") # por algun motivo, no me dejo poner el name aqui, no se, xd, pero lo aproveche bien
    while True:
        select = int(input(" ==> "))
        if select in ids:
            data_pathology.append([patient_info.title(), id_info, pathologies[temp_key[pathology_info-1]], select]) # Tu tarea es poner ese select bonito, te pasare un voice
            print(data_pathology) # Ponlo bonito x2
            break
        print("Seleccione porfavor, una opcion de verdad")

    if input("Do you want to exit?: \nY- Yes \nN - No \n").upper() == "Y": # Descubri que asi funciona
        break
