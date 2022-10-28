# 11. feladat: Szövegelemzés (4 pont)
# Írj egy szoveget_elemez nevű függvényt, amely egy szöveget vár paraméterben!
# A függvény számolja meg, hogy a szövegben mennyi betű, számjegy és egyéb karakter szerepel,
# majd adja ezt vissza egy dictionary-ben, a példában látható formátumban!
# 
# Példa:
# 
# Input: 'Python4Life!!!'
# Return: {'betu': 10, 'szamjegy': 1, 'egyeb': 3}
# 
# Input: '12345'
# Return: {'betu': 0, 'szamjegy': 5, 'egyeb': 0}

def szoveget_elemez(szoveg):
    szamjegy = 0
    betu=0
    egyeb=0
    for karakter in szoveg:
        if karakter.isdigit(): szamjegy += 1
        if karakter.isalpha(): betu += 1
        if not karakter.isalpha() and not karakter.isdigit(): egyeb+=1
    
    d = {
        "betu":betu,
        "szamjegy":szamjegy,
        "egyeb":egyeb
    }
    return d

print(szoveget_elemez('Python4Life!!!'))
print(szoveget_elemez('12345'))
