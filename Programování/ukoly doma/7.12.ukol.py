import csv

def main():
  cecka = {
      "Ema": 1,
      "Laura": 3,
      "Kuba": 4,
      "Vašek": 1,
  }
  cesta = "H:\\WET\\Programování\\python\\data.csv"
  ulozit_data(cecka, cesta)


def ulozit_data(cecka, cesta):
  with open(cesta, "w") as file:
    writer = csv.writer(file, delimiter=";")
    for jmeno, value in cecka.items():
      writer.writerow([jmeno, value])


if __name__ == "__main__":
  main()
