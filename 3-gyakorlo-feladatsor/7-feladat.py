# 7. feladat: Felváltva (5 pont)
# Írj egy felvaltva nevű függvényt, amely egy több szóból álló szöveget vár paraméterben! 
# A függvény alakítsa át a szöveget úgy, hogy az egymás utáni szavak felváltva legyenek csupa nagybetűsek, 
# illetve csupa kisbetűsek (lásd: első példa)! A szöveg első szava mindig csupa nagybetűs. A visszatérési érték az átalakított szöveg.

# Kezeld le azt az esetet, amikor a függvény egy 2-nél kevesebb szóból álló szöveget kap paraméterül! Ekkor a visszatérési érték a HIBA! szöveg legyen!

# Példa:

# Input: 'Tajekoztatjuk utasainkat, hogy a Szeged felol erkezo szemelyvonat varhatoan otven percet kesik.'
# Return: 'TAJEKOZTATJUK utasainkat, HOGY a SZEGED felol ERKEZO szemelyvonat VARHATOAN otven PERCET kesik.'

# Input: 'Sajt'
# Return: 'HIBA!'

def felvaltva(mondat):
    szavak = mondat.split(" ")
    if len(szavak) < 2: return "HIBA!"
    count = 0
    uj=""
    for szo in szavak:
        if count % 2 !=0: 
            uj+=(szo.lower()+" ")
        else:
            uj+=(szo.upper()+" ")
        count+=1
    
    return uj

print(felvaltva('Tajekoztatjuk utasainkat, hogy a Szeged felol erkezo szemelyvonat varhatoan otven percet kesik.'))
print(felvaltva('Sajt'))