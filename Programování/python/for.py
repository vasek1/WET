# for x in range(odkolika,dokolika,pokolika):
for x in range(5):
  print(x)

seznam = ["hrusky", "hranolky", "kebab", "ryze"]

for jidlo in seznam:
  print(jidlo, end="...")
print()

slovo = "ano"
print(slovo[0])

for pismeno in slovo:
  print(pismeno)

#vypisování prvního písmeno prvního slova print(seznam[0][0])
for i, polozka in enumerate(seznam):
  print(i+1, polozka)
