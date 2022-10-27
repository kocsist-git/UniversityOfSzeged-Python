# 11. feladat: Palindrom (5 pont)
# A palindrom egy olyan szó vagy szókapcsolat, amely visszafelé olvasva is ugyanaz.
# Például az "indul a görög aludni" egy híres példája a palindromoknak.

# Írj egy palindrom nevű függvényt, amely egy szöveget kap paraméterül és visszaadja,
#  hogy a paraméterben kapott szöveg palindrom-e vagy sem! A feladat megoldásának lépései:

# Először alakítsd csupa kisbetűssé a paraméterben kapott szöveget!
# Ezt követően távolítsd el a szövegből az összes szóközt, pontot, felkiáltójelet,
# kérdőjelet és vesszőt!
# Végül vizsgáld meg, hogy az így kapott szöveg megegyezik-e a megfordítottjával!

# Példa:

#Input: 'Indul a gorog aludni.'
#Return: True

#Input: 'kecske'
#Return: False

def palindrom(mondat):
    mondat=mondat.lower()
    mondat=mondat.replace(" ","")
    mondat=mondat.replace(".","")
    mondat=mondat.replace("!","")
    mondat=mondat.replace("?","")
    mondat=mondat.replace(",","")
    visszafele = mondat[::-1]

    return True if visszafele == mondat else False

print(palindrom("Indul a gorog aludni."))
print(palindrom("kecske"))