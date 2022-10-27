# 15. feladat: Szövegtömörítés (6 pont)
# Írj egy tomorit nevű függvényt, amely egy szöveget vár paraméterül!
# A függvény tömörítse a paraméterben kapott szöveget úgy, 
# hogy az egymás után lévő ismétlődő karakterek helyett az ismétlődések számát
# és az ismétlődő karaktert jelenítse meg (így például az aaabb szövegből 3a2b lesz)!
# A visszatérési érték a tömörített szöveg. A paraméterben kapott szöveg garantáltan 
# legalább 1 karakter hosszú.

# Példa:

# Input: 'Hahooooo! Van itt valaki???'
# Return: 'Hah5o! Van i2t valaki3?'

def tomorit(szoveg):
    tomoritett = ""
    szamlalo=1
    for i in range(len(szoveg)-1):
        if szoveg[i] == szoveg[i+1]:
            szamlalo+=1
        else:
            if szamlalo > 1:
                tomoritett += str(szamlalo)
                szamlalo=1
            tomoritett += szoveg[i]
    
    if szamlalo > 1:
        tomoritett += str(szamlalo) + szoveg[-1]
    else:
        tomoritett += szoveg[-1]

    return tomoritett

print(tomorit('Hahooooo! Van itt valaki???'))
print(tomorit('Hahooooo! Van itt valaki?'))
print(tomorit('aaabb'))