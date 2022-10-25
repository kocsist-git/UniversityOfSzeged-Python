ures1 = dict()  # üres dictionary létrehozása (1. verzió)
ures2 = {}      # üres dictionary létrehozása (2. verzió)

# kulcs-érték párokat tartalmazó dictionary
suti = {"nev": "dobostorta", "szeletek": 12, "elfogyott": False}

# hagyományos indexelés

print(suti["nev"])      
# print(suti["laktozmentes"])   # HIBA!!! (nem létező kulcs)

# get() metódus

print(suti.get("nev"))      
print(suti.get("laktozmentes")) # Nem letezo kulcs eseten None- ertekkel ter vissza.

suti["nev"] = "gyümölcskrémes" # Módosítás
print(suti)

suti["ar"] = 5200 # új kolcs - ertek hozzaadasa
print(suti)

del suti["szeletek"] # torles
print(suti)


if "szeletek" in suti:
    print("A süteményünk", suti["szeletek"], "szeletes.")
else:
    print("Nem tudjuk, hogy hány szeletes a süti.")

if "gyümölcskrémes" in suti.values():
    print("Ma gyümölcskrémeset eszünk.")

for kulcs in suti:
    print(kulcs)

for ertek in suti.values():
    print(ertek)

for kulcs, ertek in suti.items():
    print(kulcs, "értéke:", ertek)

my_dict = {
    1: "alma",
    2: "körte",
    3: "szilva",
    12: "alma",
    23: "körte",
    32: "szilva",
    41: "alma",
    42: "körte",
    34: "szilva"
}

# Hozzunk létre egy olyan dictionary-t, amely az értékek alapján csoportosítja a dictionary kulcsait!
# Tehát az elvárt output: {'alma': [1, 12, 41], 'körte': [2, 23, 42], 'szilva': [3, 32, 34]}

csoportok = {}
for kulcs, ertek in my_dict.items():
    # Ha létezik az adott csoportnak megfelelő lista, akkor csak beletesszük az új elemet.
    # Ha nincs még ilyen lista, akkor létrehozunk egy üres listát (get() metódus 2. paramétere), amibe beletesszük az elemet.
    csoportok[ertek] = csoportok.get(ertek, []) + [kulcs]

print(csoportok)
