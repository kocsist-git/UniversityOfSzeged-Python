# 10. feladat: Piramis (5 pont)
# Noémi, a Flying Duck Travels légitársaság utaskísérője munkájából
# kifolyólag sokat utazik a világban. Egyik kedvenc látnivalója az egyiptomi piramisok.

# Írj Python szkriptet, amely beolvas egy magasság értéket (egész szám),
# majd kirajzol a konzolra egy ilyen magas piramist * (csillag) karakterekből,
#  a példában látható formátumban! Hibakezeléssel nem kell foglalkoznod.

# Példa:

# Add meg, hogy milyen magas legyen a piramis: 5

#     *
#    ***
#   *****
#  *******
# *********


magassag = int(input("Add meg, hogy milyen magas legyen a piramis: "))

x = magassag
csillagok_szama = 1
for i in range(magassag):
    print(" "*x, "*"*csillagok_szama)
    csillagok_szama += 2
    x -= 1
