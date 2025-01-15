import csv

def main():
  cecka = {}
  cesta = "H:\\WET\\Programování\\python\\data.csv"
  nacist_data(cesta, cecka)


def nacist_data(cesta, cecka):
  with open(cesta, 'r') as soubor:
    reader = csv.reader(soubor, delimiter=";")
    for radek in reader:
      cecka[radek[0]] = int(radek[1])


if __name__ == "__main__":
  main()

