cesta = "H:\\WET\\Programování\\python\\data.txt"
#precte text
with open(cesta, "r") as soubor:
    print(soubor.read())
#prepisu soubor
with open(cesta, "w") as soubor:
    text = "jabadabaduu"
    soubor.write(text)
#prida do souboru
with open(cesta, "a") as soubor:
    text = "jabadabaduu"
    soubor.write(text)




