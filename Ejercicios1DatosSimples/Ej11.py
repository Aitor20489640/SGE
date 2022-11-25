print("Dime la cantidad de dinero depositada en la cuenta de ahorros: ", end="")
dinero = int(input())

for i in range(3):
    dinero = dinero + ((dinero * 4) / 100)
    print(f"Este es el {i + 1} año de intereses : {round(dinero, 2)}")