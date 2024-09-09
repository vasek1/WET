import csv
# cesta = "H:\\WET\\Programování\\python\\data.csv"
# with open(cesta, "r") as file:
#    reader = csv.reader(file, delimiter=";")
#    for x in reader:
#        print(x)

#pro okomentovani vic veci pravý ctrl a háček

cesta = "H:\\WET\\Programování\\python\\data.csv"
with open(cesta, "w", newline="") as file:
    jmeno = input("Zadej jmeno:")
    pocet = int(input("Zadej počet:"))
    writer = csv.writer(file, delimiter=";")
    writer.writerow([jmeno,pocet])

       