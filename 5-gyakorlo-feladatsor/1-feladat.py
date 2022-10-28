# 1. Zenék adatainak beolvasása (6 pont)
# Írj egy beolvas függvényt, amely nem vár paramétert! 
# A függvény olvassa be a playlist.csv fájl tartalmát! 
# A beolvasott sorok feldarabolása után minden zene adatait egy dictionary-ben tárold el! 
# A dictionary-k az eloado, cim, mufaj és hossz kulcsokkal rendelkezzenek, 
# amelyek közül a hossz kulcshoz tartozó érték egész szám, a többi kulcshoz tartozó érték string!
# Az így kapott dictionary-ket helyezd egy listába, majd térj vissza a listával!
# 
# A fájlkezelés során ügyelj arra, hogy a megnyitott fájl minden esetben biztonságosan le legyen zárva!
# Ehhez használd a gyakorlaton tanult, kontextus-kezelős megoldást!
# 
# A függvény elvárt visszatérési értéke:
# 
# [
#     {'eloado': 'Rick Astley', 'cim': 'Never Gonna Give You Up', 'mufaj': 'pop', 'hossz': 213}, 
#     {'eloado': 'Imagine Dragons', 'cim': 'Thunder', 'mufaj': 'pop', 'hossz': 204}, 
#     {'eloado': 'Dragonforce', 'cim': 'Through the Fire and Flames', 'mufaj': 'metal', 'hossz': 445}, 
#     {'eloado': 'Boney M.', 'cim': 'Rasputin', 'mufaj': 'pop', 'hossz': 284}, 
#     {'eloado': 'Steppenwolf', 'cim': 'Born To Be Wild', 'mufaj': 'rock', 'hossz': 216}, 
#     {'eloado': 'Powerwolf', 'cim': 'Incense and Iron', 'mufaj': 'metal', 'hossz': 240}, 
#     {'eloado': 'Smash Mouth', 'cim': 'All Star', 'mufaj': 'rock', 'hossz': 237}, 
#     {'eloado': 'Nirvana', 'cim': 'Smells Like Teen Spirit', 'mufaj': 'rock', 'hossz': 279}, 
#     {'eloado': 'Gloryhammer', 'cim': 'The Unicorn Invasion of Dundee', 'mufaj': 'metal', 'hossz': 265}, 
#     {'eloado': 'Powerwolf', 'cim': 'Venom of Venus', 'mufaj': 'metal', 'hossz': 208}, 
#     {'eloado': 'Imagine Dragons', 'cim': 'Radioactive', 'mufaj': 'rock', 'hossz': 188}, 
#     {'eloado': 'Dschinghis Khan', 'cim': 'Moskau', 'mufaj': 'pop', 'hossz': 275}, 
#     {'eloado': 'Dschinghis Khan', 'cim': 'Dschinghis Khan', 'mufaj': 'pop', 'hossz': 185}, 
#     {'eloado': 'Bonnie Tyler', 'cim': 'Total Eclipse of the Heart', 'mufaj': 'pop', 'hossz': 334}, 
#     {'eloado': 'Gopnik McBlyat', 'cim': 'Snakes In Tracksuits', 'mufaj': 'hardbass', 'hossz': 261}, 
#     {'eloado': 'Foster The People', 'cim': 'Pumped Up Kicks', 'mufaj': 'pop', 'hossz': 253}, 
#     {'eloado': 'Linkin Park', 'cim': 'In The End', 'mufaj': 'rock', 'hossz': 219}, 
#     {'eloado': 'Powerwolf', 'cim': 'Dancing With The Dead', 'mufaj': 'metal', 'hossz': 291}, 
#     {'eloado': 'Green Day', 'cim': 'Boulevard of Broken Dreams', 'mufaj': 'rock', 'hossz': 288}, 
#     {'eloado': 'Korpiklaani', 'cim': 'Ievan polkka', 'mufaj': 'metal', 'hossz': 194}
# ]

def beolvas():
    eredmeny = list()
    with open("playlist.csv", "r") as f:    
        sor = f.readline()
        while sor:
            adatok = sor.split(";")
            sor_Dict = {
                "eloado":adatok[0],
                "cim":adatok[1],
                "mufaj":adatok[2],
                "hossz":int(adatok[3])
            }
            eredmeny.append(sor_Dict)
            sor = f.readline()
    return eredmeny

def teljes_hossz(lista):
    hossza = 0
    for sor in lista:
        hossza += sor.get("hossz")
    
    with open("02_hossz.txt", "w") as file:
        file.write(f"A lejatszasi lista hossza: {hossza//60} perc, {hossza%60} masodperc")
    return f"A lejatszasi lista hossza: {hossza//60} perc, {hossza%60} masodperc"

def leghosszabb_rockzene(lista):
    max_hossz=0
    gyoztes = ""
    for sor in lista:
        if sor.get("mufaj") == "rock" and sor.get("hossz") > 0:
            max_hossz = sor.get("hossz")
            gyoztes = sor.get("cim")

    with open("03_leghosszabb_rock.txt", "w") as file:
        file.write(gyoztes)
    
    return gyoztes

def leggyakoribb_mufaj(lista):
    eredmeny = dict()
    for sor in lista:
        for kulcs, ertek in sor.items():
            if kulcs == "mufaj":
                if ertek in eredmeny:
                    eredmeny[ertek] +=1
                else:
                    eredmeny[ertek] = 1
    
    max_szerepelt=0
    gyoztes = ""
    for mufaj, haszor in eredmeny.items():
        if max_szerepelt < haszor:
            max_szerepelt = haszor
            gyoztes = mufaj
    
    with open("04_kedvenc_mufaj.txt", "w") as f:
        f.write(gyoztes.upper())

    return gyoztes.upper()

print(beolvas())
print(teljes_hossz(beolvas()))
print(leghosszabb_rockzene(beolvas()))
print(leggyakoribb_mufaj(beolvas()))

