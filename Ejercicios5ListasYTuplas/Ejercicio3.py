asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

for i in asignaturas:
    notas.append(input(f"Que nota has sacado en {i}: "))

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")