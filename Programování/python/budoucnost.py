import random

odpoved = random.randint(0,4)



'''
if cislo == 1:
  print("ano")
elif cislo == 2:
  print("ne")
elif cislo == 3:
  print("mozna")
elif cislo == 4:
  print("urcite")
elif cislo == 5:
  print("stopro")
'''
odpovedi = ["ano","stopro","ne", "mozna","urcite ne"]

while True:
  otazka = input("Na co se chces zeptat\n")
  if otazka== "konec":
    break
  odpoved = random.randint(0,4)
  print(odpovedi [odpoved])
