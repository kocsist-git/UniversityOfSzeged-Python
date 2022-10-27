# 14. feladat: Mocking Spongebob (4 pont)
# Ki ne emlékezne az alábbi meme template-re és annak jellegzetes szövegformátumára?
# A feladat egy olyan függvény írása, amely egy megadott szöveget a képen látható formátumra
# alakít át.

# Mocking Spongebob meme

# Hozz létre egy mocking_spongebob nevű függvényt, amely egy szöveget kap paraméterül!
# A függvény alakítsa át a szöveget úgy, hogy a páros indexeken lévő karakterek kisbetűvel,
# míg a páratlan indexeken lévő karakterek nagybetűvel jelenjenek meg!
# A visszatérési érték az átalakított szöveg.

# Példa:

# Input: 'A Szkriptnyelvek meg konnyu targynak szamit.'
# Return: 'a sZkRiPtNyElVeK MeG KoNnYu tArGyNaK SzAmIt.'

def mocking_spongebob(szoveg):
    uj_szoveg = ""
    counter=2
    for betu in szoveg:
        if counter %2 == 0: 
            uj_szoveg += betu.lower()
        else:
            uj_szoveg += betu.upper()
        counter += 1
    return uj_szoveg

print(mocking_spongebob('A Szkriptnyelvek meg konnyu targynak szamit.'))