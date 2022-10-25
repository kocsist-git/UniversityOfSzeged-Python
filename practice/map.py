def formazas(s):
    return s.rstrip().title()

szavak = ["sor", "karacsonyfa", "to", "ajandek", "gesztenyekocka"]

formazott_szavak = list (map(formazas, szavak))
print(formazott_szavak)

szamok = list(map(int, ["12", "3","-15"]))
print(szamok)