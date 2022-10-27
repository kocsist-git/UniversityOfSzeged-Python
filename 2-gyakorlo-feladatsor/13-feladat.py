# 13. feladat: Idegesség detektor (5 pont)
# Zsófi az egyik egyetemi projektjében CooSpace kommenteket elemez. 
# A feladat egy egyszerű algoritmus írása, amely a komment szövege alapján eldönti, 
# hogy a kommentet író felhasználó ideges lehetett-e a kommentírás pillanatában.

# Írj egy idegesseg_detektor nevű függvényt, amely egy komment szövegét várja paraméterül! 
# A függvény számolja meg, hogy összesen hány nagybetű és felkiáltójel (!) 
# szerepel a komment szövegében, majd az így kapott eredményt ossza el a komment 
# szövegének hosszával! Ha az így kapott arányszám 0.5-nél nagyobb, akkor a függvény logikai igaz,
# egyébként pedig logikai hamis értékkel térjen vissza!

# Kezeld le azt az esetet, amikor a komment szövege egyetlen karaktert sem tartalmaz! 
# Ekkor a függvény None beépített értékkel térjen vissza!

# Példa:

# Input: 'Hello! 3 darab AUCHANOS ZSEMLET cserelnek SURGOSEN kedd esti PROG2 gyakorlatra.'
#Return: False

# Input: 'KEDVES FERENC! Az EN VELEMENYEM pedig az, hogy a FELADAT KESZITOJE KIFOGYOTT
#  az ERTELMES peldamondatokbol!!!!!!'
# Return: True

# Input: ''
# Return: None

def idegesseg_detektor(szoveg):
    darab = szoveg.count("!")
    for betu in szoveg:
        if betu.isupper(): darab+=1
    return True if (darab/len(szoveg)) > 0.5 else False
print(idegesseg_detektor('Hello! 3 darab AUCHANOS ZSEMLET cserelnek SURGOSEN kedd esti PROG2 gyakorlatra.'))
print(idegesseg_detektor('KEDVES FERENC! Az EN VELEMENYEM pedig az, hogy a FELADAT KESZITOJE KIFOGYOTT az ERTELMES peldamondatokbol!!!!!!'))