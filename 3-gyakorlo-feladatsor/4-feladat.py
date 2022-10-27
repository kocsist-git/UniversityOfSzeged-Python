# 4. feladat: Leghosszabb szó (3 pont)
# Írj egy leghosszabb_szo nevű függvényt, amely egy szöveget kap paraméterül (a szöveg szóközzel elválasztott szavakat tartalmaz)! 
# A függvény térjen vissza a szövegben található leghosszabb szóval!
# Amennyiben több szó is ugyanolyan hosszú, akkor közülük a szövegben korábban előfordulót add vissza!

# Ha a paraméterül kapott szöveg az üres string, akkor a visszatérési érték a HIBA! szöveg legyen!

# Példa:

# Input: 'Szia uram! Mondd mar meg, hogy hany ora van!'
# Return: 'uram!'

# Input: ''
# Return: 'HIBA!'

def leghosszabb_szo(szoveg):
    if szoveg == "": return "HIBA!"
    lista = szoveg.split(" ")
    leghosszabb = ""
    for szo in lista:
        if len(szo) > len(leghosszabb): leghosszabb = szo
    return leghosszabb


print(leghosszabb_szo("Szia uram! Mondd mar meg, hogy hany ora van!"))
print(leghosszabb_szo(""))
