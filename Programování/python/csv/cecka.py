import csv
cesta = "H:\\WET\\Programování\\python\\csv\\data.csv"
def main():
  cecka = {}

 

  print("Vítej v Bradavicích")
  print("Zvol možnost:")
  print("Pro vypsání všech ceček zvol 1")
  print("Pro vypsání jednoho studenta zvol 2")
  print("Pro přidání  cečka zvol 3")
  print("Pro odebrání cečka ceček zvol 4")
  print("Pro přidání studenta zvol 5")

  zvolena_moznost = int(input())

  match zvolena_moznost:
      case 1: 
        vypisVse(cecka)
      case 2:
        vypis_cecka(cecka)
      case 3:
        pridejcecka(cecka)
      case 4:
        odebercecka(cecka)
      case 5:
        pridejStudenta(cecka)
      case _:
        print("Zvol číslo mezi 1-5")

  vypisVse(cecka)


def vypis_cecka(cecka):
  jmeno = input("Koho chceš zkontrolovat ?").capitalize()
  if jmeno in cecka:  
      print(jmeno,cecka[jmeno])

def vypisVse(cecka):
   for vsichni in cecka:
    print(vsichni,cecka[vsichni])

def pridejcecka(seznam,jmeno):
  jmeno = input("Komu chces pridat cecka ?").capitalize()
  if jmeno in seznam:  
      print(jmeno, seznam[jmeno]+1)

def odebercecka(seznam,jmeno):
  jmeno = input("Komu chces odebrat cecka ?").capitalize()
  if jmeno in seznam:  
      print(jmeno, seznam[jmeno]-1)

def pridejStudenta(cecka,jmeno):
  jmeno = input("Pridej studentku:").capitalize()
  cecka[jmeno] = 1
  print(jmeno, cecka[jmeno])
  cecka.update({jmeno:1})
 
def ulozit_data(cecka):
  with open(cesta, "w") as file:
    writer = csv.writer(file, delimiter=";")
    for jmeno, value in cecka.items():
      writer.writerow([jmeno, value])


def nacist_data(cecka):
  with open(cesta, 'r') as soubor:
    reader = csv.reader(soubor, delimiter=";")
    for row in reader:
      cecka[row[0]] = int(row[1])



if __name__ == "__main__":
  main()