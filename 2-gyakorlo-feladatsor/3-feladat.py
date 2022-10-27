# 3. feladat: Kuba (2 pont)
# Kuba egy Discord szerveren moderátor. A szabadidejét sokszor azzal tölti, hogy 
# a szerver bizonyos tagjainak a felhasználónevét átírja a következőképpen:

# a felhasználónév végére egy . (pont) karaktert tesz, amennyiben az eredetileg nem végződött pontra
# ellenkező esetben, pont karakterre végződő felhasználónevek esetén eltávolítja a név végéről a pontot.
# Írj egy kuba nevű függvényt, amely egy felhasználónevet (string) kap paraméterül, 
# elvégzi a fenti szabályok alapján a név átalakítását, majd visszatér az így kapott eredménnyel!

# Példa:

# Input: 'Korte12'
# Return: 'Korte12.'

# Input: 'Tamas.'
#Return: 'Tamas'

def kuba(nev):
    if nev[-1] == ".":
        return nev[:len(nev)-1]
    else:
        return nev + "."

print(kuba("Korte12"))
print(kuba("Tamás."))