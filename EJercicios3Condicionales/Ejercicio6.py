genero = input("Escribe si eres hombre o mujer: ")
nombre = input("Escribe tu nombre: ")

if nombre[0].upper() < "M" and genero.lower() == "mujer" or nombre[0].upper() > "N" and genero.lower() == "hombre":
    print("Estas en el grupo A")
else:
    print("Estas en el grupo B")
