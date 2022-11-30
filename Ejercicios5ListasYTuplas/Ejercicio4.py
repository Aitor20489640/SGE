numerosPrimitiva = []

for i in range(6):
    numerosPrimitiva.append(int(input("Dime los números ganadores de la primitiva: ")))

numerosPrimitiva.sort()
for i in numerosPrimitiva:
    print(i)
