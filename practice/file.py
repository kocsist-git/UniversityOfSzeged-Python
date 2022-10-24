# Nem az operacios rendszer vegzi el a fajl megnyitasat, hanem a python maga

f = open("t.txt","r", encoding="utf-8")
# r : olvasasra (alapertelmezett)
# w : irasra
# a : hozzafuzes
# b : binaris mod
# t : szoveges mod 
# x : kizarolagos fajl letrehozas

fajl_tartalma = f.read()

print(fajl_tartalma)

f.close()

# Gyakori muveletek

# read()
# read(x) x karaktert olvas be
# readline() egy sor beolvasasa
# readlines() az egesz fajl beolvasasa soronkent
# write(string) szoveg kiirasa a fajlba
# tell() visszaadja, az aktualis poziciot a fajlba
# seek(szam, honnan) poziciovaltas a fajlban
    # honnan 0 a file eleje
           # 1 az aktualis pozi
           # 2 a fajl vege
# close() megnyitott fajl lezarasa 


