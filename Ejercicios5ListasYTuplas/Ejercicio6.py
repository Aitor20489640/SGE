asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
passed = []

for i in asignaturas:
    nota = int(input(f"Que nota has sacado en {i}: "))
    if nota >= 5:
        passed.append(i)

for i in passed:
    asignaturas.remove(i)

print(f"Tienes que repetir {asignaturas}")