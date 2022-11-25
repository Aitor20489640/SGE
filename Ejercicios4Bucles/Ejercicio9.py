encontrado = False
string = "contraseña"
while not encontrado:
    palabra=input("Adivina la contraseña: ")
    if palabra == string:
        print("La adivinaste")
        encontrado = True
