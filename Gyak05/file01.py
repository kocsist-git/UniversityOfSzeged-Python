# open(path, mode): fájl megnyitása
# path: a megnyitni kívánt fájl elérési útvonala (szöveg)
# mode: a fájlmegnyitás módja (szöveg)
#   "r": olvasásra (alapértelmezett)
#   "w": írásra (felülírja a fájl korábbi tartalmát)
#   "a": fájl végéhez való hozzáfűzésre (megőrzi a fájl korábbi tartalmát)
#   "x": kizárólagos létrehozásra (ha már létezik a fájl, akkor hibát kapunk)
# egy fájlt megnyithatunk szöveges ("t") vagy bináris ("b") módban - ezek közül 
# a szöveges mód az alapértelmezett, mi is mindig ezt fogjuk használni

# read(n): n darab karakter beolvasása (ahol éppen vagyunk a fájlban)
# readline(): egy sor beolvasása (ahol éppen vagyunk a fájlban)
# readlines(): az egész fájl beolvasása, soronként
# write(szoveg): adott szöveg írása fájlba
# close(): a megnyitott fájl lezárása

# a be.txt fájl megnyitása olvasásra
file = open("be.txt", "r")      

# a teljes fájl tartalmának beolvasása
tartalom = file.readlines()

# a tartalom kiíratása soronként
for sor in tartalom:
    sor = sor.rstrip()      # sorvége-jel eltávolítása
    print(sor)

# a megnyitott fájl lezárása
file.close()                    

####################-----------------------------------####################

try:
    file = open("be.txt", "r")
    tartalom = file.readlines()

    for sor in tartalom:
        sor = sor.rstrip()
        print(sor)

    file.close()
except FileNotFoundError as fnfe:
    print("A fájl nem található!")


####################-----------------------------------####################

atlag = 0                       # változó az átlagnak

with open("be02.txt", "r") as f:  # be.txt megnyitása olvasásra
    osszeg = 0                  # a beolvasott számok összege (az átlaghoz kell)
    darab = 0                   # hány számot olvastunk be (az átlaghoz kell)

    sor = f.readline()          # első sor beolvasása

    while sor:                  # amíg van sor a fájlban...
        osszeg += int(sor)      # ...hozzáadjuk az adott számot az összeghez
        darab += 1              # ...növeljük a beolvasott számok darabszámát
        sor = f.readline()      # ...beolvassuk a következő sort

atlag = osszeg / darab          # az átlag az összeg és a darabszám hányadosa

with open("ki.txt", "w") as f:  # ki.txt megnyitása írásra
    f.write("Az átlag: " + str(atlag) + "\n")  # az eredmény fájlba írása
