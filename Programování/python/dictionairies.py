pes = {"barva":"hneda",
       "jmeno" : "Moriz",
        "oblibene_jidlo":["pizza", "ryba podle Petra Voka"],
        "povaha":"hňup",
        "nohy": 1,
        "žije": True
       }
print(pes["jmeno"])
print(pes["oblibene_jidlo"][0])
for jidlo in pes["oblibene_jidlo"]:
    print(jidlo)

tel_seznam = {
    "Jarmil" : "735 552 556",
    "Vasek" : "786 222 111",
    "Kuba" : "+ 420 735 552 556",
    "Lauros" : "+ 420 752 592 556"
}