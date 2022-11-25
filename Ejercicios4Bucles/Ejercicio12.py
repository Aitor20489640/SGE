palabra=input("Escribe una palabra: ")
letra=input("Escribe una letra: ")
cont=0

for i in palabra:
    if i.lower() == letra[0].lower():
        cont += 1
print(f"La letra {letra} ha aparecido {cont} veces.")
