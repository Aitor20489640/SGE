print("Dime  los productos de una cesta de la compra, separados por comas")
cestaCompras = input()
listaCompras = cestaCompras.split(",")

for i in listaCompras:
    print(i)