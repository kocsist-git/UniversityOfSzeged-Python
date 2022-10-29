# https://cservz.github.io/teaching/szkriptnyelvek/feladatsorok/05/


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

def zeneket_csoportosit(lista):
    csoport = dict()
    for eloadok in lista:
        if eloadok["eloado"] in csoport:
            csoport[eloadok["eloado"]] += eloadok["hossz"]
        else:
            csoport[eloadok["eloado"]] = eloadok["hossz"]
    
    with open("05_osszegzes.txt", "w") as f:
        for kulcs, ertek in sorted(csoport.items()):
            f.writelines(f"{kulcs} - osszesen {ertek} masodpercnyi zene\n")
    return sorted(csoport.items())

def zeneket_listaz(lista, eloado):
    eloado2=eloado.replace(" ", "_").lower()
    kiir=""
    for szam in lista:
        if szam["eloado"].lower() == eloado.lower():
            kiir += szam["cim"] + ";" + szam["mufaj"] +";"+ str(szam["hossz"]) + "\n"
    with open (f"06_{eloado2}_dalok.txt","w") as f:
        if kiir == "": kiir="Nincs ilyen eloado a listaban!"
        f.writelines(kiir)

    return kiir

def zeneket_torol(lista, eloadok):
    kiir=""
    for szam in lista:
        if szam["eloado"] not in eloadok:
            kiir += szam["eloado"] + ";" + szam["cim"] + ";" + szam["mufaj"] +";"+ str(szam["hossz"]) + "\n"
    with open("07_torolt.txt","w") as f:
        f.writelines(kiir)

print(beolvas())
print(teljes_hossz(beolvas()))
print(leghosszabb_rockzene(beolvas()))
print(leggyakoribb_mufaj(beolvas()))
print(zeneket_csoportosit(beolvas()))
print(zeneket_listaz(beolvas(), "Imagine Dragons"))
print(zeneket_listaz(beolvas(), "POWERWOLF"))
print(zeneket_listaz(beolvas(), "Taylor Swift"))
zeneket_torol(beolvas(),['Imagine Dragons', 'Rick Astley', 'Powerwolf'])