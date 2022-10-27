# 10. feladat: Elmozdulás (5 pont)
# Írj egy elmozdulas nevű függvényt, amely egy útvonalat elkódoló szöveget kap paraméterül! 
# A szövegben előforduló betűk és jelentésük:
# F (1 lépést megyünk felfelé),
# L (1 lépést megyünk lefelé),
# J (1 lépést megyünk jobbra),
# B (1 lépést megyünk balra).

# A függvény adja vissza a példában látható formátumban azt, 
# hogy a kiinduló pozíciónkhoz képest, az útvonal követésével mennyit megyünk a vízszintes, 
# illetve a függőleges irányba! Ha az útvonal követésével a kiinduló pozícióba érünk vissza, 
# akkor a függvény a Nem mentunk sehova szöveggel térjen vissza!

# Például, ha az útvonalunk a JBBFB, akkor 1 lépést mentünk jobbra, 
# majd 2-t balra, 1-et fel és végül 1-et balra. Így az eredeti pozíciónkhoz képest 2 lépéssel 
# kerültünk balra és 1 lépéssel kerültünk feljebb.

# Példa:

# Input: 'JJFBFFFFFFBBBL'
# Return: '2 lepes balra, 6 lepes fel'

# Input: 'FBLLLJLLJ'
# Return: '1 lepes jobbra, 4 lepes le'

# Input: 'FFF'
# Return: '3 lepes fel'

# Input: 'FFLLBBJJ'
# Return: 'Nem mentunk sehova'

def elmozdulas(uzenet):
    x=0
    y=0
    for betu in uzenet:
        if betu == "J":
            x+=1
        elif betu == "B":
            x-=1
        elif betu == "F":
            y+=1
        elif betu == "L":
            y-=1
    irany = ""
    if x > 0:
        irany=str(x) + " lepes jobbra, "
    elif x < 0:
        irany=str(abs(x)) + " lepes balra, "
    if y > 0:
        irany+=str(y) + " lepes fel"
    else:
        irany+=str(abs(y)) + " lepes le"

    if x == 0 and y ==0:
        irany = 'Nem mentunk sehova'

    return irany 
print(elmozdulas('JJFBFFFFFFBBBL'))
print(elmozdulas('FBLLLJLLJ'))
print(elmozdulas('FFF'))
print(elmozdulas('FFLLBBJJ'))