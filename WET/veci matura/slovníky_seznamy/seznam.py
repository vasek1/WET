seznam_ovoce =["jablko", "pomeranč","banán"]

seznam_ovoce.append("kiwi")

print(seznam_ovoce[1])

print(len(seznam_ovoce))# dává délku seznamu

seznam_ovoce[0] = "hruška"
odebrane = seznam_ovoce.pop(1) #odebrání ovoce
print(f"Bylo odebran {odebrane}")

for index, ovoce in enumerate(seznam_ovoce):
    print(f"{index+1}. {ovoce}")

if "kiwi" in seznam_ovoce:
    print("ano")