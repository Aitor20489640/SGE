palabra = input("Dime una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    cont = 0
    for letra in palabra:
        if letra == vocal:
            cont += 1
    print(f"La {vocal} ha aparecido {cont} veces")
    