# 8. feladat: Szöveg titkosítása (3 pont)
# Robi és Misi jó barátok, sőt történetesen ugyanannál a cégnél munkatársak.
# Kitalálták, hogy azért, hogy a főnökük ne érthesse meg az egymásnak írt üzeneteiket,
# egy egyszerű titkosítást használnak. A küldő kódolja az üzenetet az elküldés előtt,
# a fogadó pedig visszafejti azt.

# Írj egy kodol nevű függvényt, amely 3 paramétert kap: rendre a titkosítandó üzenetet,
# egy n pozitív egész számot, valamint egy c karaktert. A függvény alakítsa át az üzenetet úgy,
# hogy az üzenet minden betűje után n darab c karaktert tegyen! A függvény visszatérési értéke a
# kódolt üzenet.

# Példa:

# Input: 'Pizza delben?', 3, 'x'
# Return: 'Pxxxixxxzxxxzxxxaxxx xxxdxxxexxxlxxxbxxxexxxnxxx?xxx'

def kodol(uzenet, mennyi, karakter):
    szoveg = ""
    for betu in uzenet:
        mit = karakter*mennyi
        szoveg += betu + mit
    return szoveg

print(kodol('Pizza delben?', 3, 'x'))