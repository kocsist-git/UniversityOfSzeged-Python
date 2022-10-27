# 12. feladat: Palindromszám (3 pont)
# Az előző feladatban szereplő definíció alapján könnyedén kitalálható, 
# hogy mik a palindromszámok: olyan számok, amelyek számjegyeit visszafelé
# olvasva az eredeti számot kapjuk.

# Írj egy palindromszam nevű függvényt, amely garantáltan egy pozitív egész számot kap paraméterül, 
# és visszaadja, hogy ez a szám palindromszám-e vagy sem!

# Példa:

# Input: 123454321
# Return: True

# Input: 2020
# Return: False

def palindromszam(szam):
    return True if szam == int(str(szam)[::-1]) else False

print(palindromszam(123454321))
print(palindromszam(2020))