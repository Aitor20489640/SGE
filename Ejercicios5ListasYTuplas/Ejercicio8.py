palabra = input("Escribe una palabra: ")
if palabra == palabra[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")