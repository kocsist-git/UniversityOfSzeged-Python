ures1 = list()      # üres lista létrehozása (1. verzió)
ures2 = []          # üres lista létrehozása (2. verzió)

kutyak = ["Ubul", "Snoopy", "Scooby Doo"]   # stringeket tároló lista

gyumolcsok = ["alma", "citrom", "barack", "pomeló"]

print(gyumolcsok[0])        # a legelső listaelem
print(gyumolcsok[-1])       # az utolsó listaelem
print(gyumolcsok[1:3])      # az 1-3. indexű elemek (a 3. indexű elem már nincs benne)
print(gyumolcsok[2:])       # az elemek a 2. indextől a lista végéig
print(gyumolcsok[:])        # a teljes lista
print(gyumolcsok[::2])      # minden második listaelem

gyumolcsok = ["alma", "citrom", "barack", "pomeló"]
print(gyumolcsok[::-1]) # lista megforditasa

gyumolcsok[1] = "görögdinnye"       # listaelem módosítása
print(gyumolcsok)

for gyumi in gyumolcsok:            # listaszerű for ciklus
    print(gyumi)

print("--------------------")

for i in range(len(gyumolcsok)):    # index alapú for ciklus
    print(gyumolcsok[i])

# Ha az elemeket módosítani szeretnénk a bejárás során, akkor az index alapú bejárást válasszuk!

# A listak referenciakent kerulnek atadasra
def nagybetusit(lista):
    for i in range(len(lista)): # egy stringekből álló lista összes elemét nagybetűsítjük
        lista[i] = lista[i].upper()

    return lista

nagybetus_gyumolcsok = nagybetusit(gyumolcsok)

print(nagybetus_gyumolcsok)
print(gyumolcsok)               # az eredeti lista is módosul!

#########

def nagybetusit(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()

    return lista

gyumolcsok = ["alma", "citrom", "barack", "pomeló"]
nagybetus_gyumolcsok = nagybetusit(gyumolcsok[:])   # egy másolatot adunk át

print(nagybetus_gyumolcsok)
print(gyumolcsok)               # az eredeti lista tartalma megmarad!


bosszuallok = ["Thor", "Hulk", "Vízió", "Hangya", "Vasember"]

if "Hulk" in bosszuallok:
    print("Hulk a bosszúállók közé tartozik.")


bosszuallok = ["Thor", "Hulk", "Vízió", "Hangya", "Vasember"]
del bosszuallok[2]

print(bosszuallok)


bosszuallok1 = ["Thor", "Hulk", "Vízió"]
bosszuallok2 = ["Hangya", "Vasember"]

osszefuzott = bosszuallok1 + bosszuallok2
print(osszefuzott)

bosszuallok1 = ["Thor", "Hulk", "Vízió"]
bosszuallok2 = ["Hangya", "Vasember"]

bosszuallok1.extend(bosszuallok2) # ez is egy osszefuzes
print(bosszuallok1)

# lista.append(e): beszúrja az e elemet a lista végére
# lista.insert(i, e): beszúrja az e elemet a lista i. indexére
# lista.remove(e): törli a lista-ból az e elem legelső előfordulását
# lista.sort(): rendezi a lista elemeit
#   helyben rendez, így az eredeti listát módosítja (ha ezt nem szeretnénk, akkor használhatjuk a sorted(lista) függvényt)
#   többféle adattípusra is működik: szövegeket tartalmazó listákat ábécé-sorrendbe, számokat tartalmazó listákat növekvő sorrendbe rendezi alapértelmezés szerint
# lista.clear(): kiüríti a lista-t.

bosszuallok = ["Thor", "Hulk", "Vízió", "Thor"]

bosszuallok.append("Hangya")        # hozzáfűzés a lista végéhez
print(bosszuallok)
bosszuallok.insert(0, "Vasember")   # beszúrás a lista elejére
print(bosszuallok)

bosszuallok.remove("Thor")          # a legelső "Thor"-t törli
bosszuallok.sort()                  # rendezés (itt: ábécé-sorrend)
print(bosszuallok)

bosszuallok.clear()                 # lista kiürítése
print(bosszuallok)

#############

szoveg = "A Python egy nagyon klassz nyelv!"
szavak = szoveg.split(" ")          # szöveg feldarabolása szóközök mentén

print(szavak)

gyumolcsok = ["alma", "citrom", "barack", "pomeló"]

print(" ".join(gyumolcsok))     # szöveggé egyesítés szóköz karakterek mentén
print(";".join(gyumolcsok))     # szöveggé egyesítés pontosvesszők mentén
print(" --- ".join(gyumolcsok)) # tetszőleges karaktersorozatot is megadhatunk

