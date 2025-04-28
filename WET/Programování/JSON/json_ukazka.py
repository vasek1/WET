import json

filmy = {"komedie":"Tropická bouře",
         "horror":["Smile,It"],
         "animák":["Spongebob","Lví král"]
         }

with open("data.json", mode="w") as soubor:
    json.dump(filmy,soubor, indent=4, ensure_ascii = False)

with open("data.json", mode="r") as soubor: # otevře soubor a poté ho automaticky zavře
    nactenadata = json.load(soubor)
print(nactenadata)
