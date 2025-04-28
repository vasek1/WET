tel_seznam={
    "Jarmil":"777",
    "Petr": "666",
    "Adam": "555"
}

for key in tel_seznam.keys():
    print(key)
for x in tel_seznam:
    print(x)

#pro vypsání telefoního čísla 2 způsoby
for v in tel_seznam.values():
    print(v)

for y in tel_seznam:
    print(tel_seznam)
#obojí
for key, value in tel_seznam.items():
    print(key, value)

tel_seznam.get("Kazi", "nic")