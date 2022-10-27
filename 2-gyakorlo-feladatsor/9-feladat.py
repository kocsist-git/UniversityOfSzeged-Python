# 9. feladat: Titkosított szöveg visszafejtése (2 pont)
# Természetesen Robi és Misi kommunikációjához fontos, hogy 
# a két kolléga vissza tudja fejteni egymás kódolt üzeneteit.

# Írj egy dekodol nevű függvényt, amely 2 paramétert kap:
# rendre a kódolt szöveget és egy n pozitív egész számot! 
# A szöveget úgy tudjuk dekódolni, hogy a szöveg első karakterétől indulunk,
# mindig kihagyunk n darab karaktert, és a nem kihagyott karaktereket összeolvassuk.
# A függvény visszatérési értéke a dekódolt szöveg.

# Példa:

# Input: 'Pxxxixxxzxxxzxxxaxxx xxxdxxxexxxlxxxbxxxexxxnxxx?xxx', 3
# Return: 'Pizza delben?'

def kodol(uzenet, mennyi):
    return uzenet[::mennyi+1]

print(kodol('Pxxxixxxzxxxzxxxaxxx xxxdxxxexxxlxxxbxxxexxxnxxx?xxx', 3))