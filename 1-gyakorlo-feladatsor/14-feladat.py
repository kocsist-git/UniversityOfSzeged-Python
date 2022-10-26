# 14. feladat: Időkülönbség (5 pont)
# Zhang miniszter az idő megszállottja: minden napjának időbeosztását előre megtervezi a lehető legnagyobb precizitással. 
# Sajnos Zhang nem jó fejszámolásban, így sokszor bajban van, amikor egy megbeszélésének az időtartamát kell kiszámolni
# a megbeszélés kezdetének és végének az időpontja alapján.

# Írj Python szkriptet, amely kiszámítja egy nap két időpontja közötti időkülönbséget!
# Olvasd be a két időpontot (óra és perc, mindketten egész számok) a példában látható formátumban,
# majd írasd ki a köztük lévő időkülönbséget (óra és perc)! Előfordulhat, 
# hogy az első időpont a későbbi (lásd: második példa)! Egyéb hibakezeléssel nem kell foglalkoznod.

# A feladat megoldása során ne használj semmilyen beépített vagy külső Python csomagot!

# Példa:

# Elso idopont (ora): 8
# Elso idopont (perc): 15
# Masodik idopont (ora): 16
# Masodik idopont (perc): 0

# A ket idopont kozott 7 ora es 45 perc telt el.
# Elso idopont (ora): 10
# Elso idopont (perc): 30
# Masodik idopont (ora): 8
# Masodik idopont (perc): 30

# A ket idopont kozott 2 ora es 0 perc telt el.

ora1 = int(input("Elso idopont (ora): "))
perc1 = int(input("Elso idopont (perc): "))

ora2 = int(input("Masodik idopont (ora): "))
perc2 = int(input("Masodik idopont (perc): "))

ido1 = ora1*60 + perc1
ido2 = ora2*60 + perc2

eltelt = abs(ido1-ido2)

ora = eltelt // 60
perc = eltelt % 60

print(f"A ket idopont kozott {ora} ora es {perc} perc telt el.")