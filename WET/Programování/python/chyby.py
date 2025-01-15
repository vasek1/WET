import sys

def kladne_zaporne(x):
    if x >0:
        print("číslo je kladné")
    elif x<0:
        print("číslo je záporné")
    else:
        print("číslo je 0")
while True:
    try:
        cislo = int(input("Zadej číslo:"))
        kladne_zaporne(cislo)
    except KeyboardInterrupt:
        print("funguje")
        sys.exit()
        
    except ValueError:
        print("Špatný input... zadal si číslo")
    else:
        print("kod proběhl úspěšně")
       
    finally:
        print("vypíše se vždy")