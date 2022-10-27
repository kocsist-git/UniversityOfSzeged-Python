# 6. feladat: Jelszó-erősség mérő (5 pont)
# Elliot egy kiberbiztonsági cégnél dolgozik. Egyik nap a felettese egy jelszó-erősség mérő szkript írásával bízta meg. Készíts egy jelszo_erosseg nevű függvényt, amely egy jelszót (string) kap paraméterül, és visszaadja, hogy a jelszó mennyire erős! Szabályok a jelszó-erősség meghatározására:

# Alapból minden jelszó 1 erős
# Legalább 5 karakter hosszú jelszó: +1 erősség
# Legalább 8 karakter hosszú jelszó: +2 erősség
# A jelszóban szereplő minden alulvonás, kötőjel vagy pont karakter 2-vel növeli a jelszó erősségét
# Ha a jelszó tartalmazza a jelszo vagy az 123 részszöveget, akkor automatikusan 0 erős
# Ha a jelszó 0 karakter hosszú, akkor szintén automatikusan 0 erős.
# Példa:

# Input: 'hazi_macska_4_life'
# Return: 10

#Input: 'ez1feltorhetetlenjelszo'
#Return: 0

def jelszo_erosseg (jelszo):
    
    if len(jelszo) == 0 or jelszo.count("jelsz") or jelszo.count("123"):
        return 0
    else:
        eros = 1
        if 5 <= len(jelszo) <= 7:
            eros +=1
        elif len(jelszo) >= 8:
            eros +=2
        
        for betu in jelszo:
            if betu == "_" or betu == "-" or betu == ".":
                eros+=2
        return eros

print(jelszo_erosseg("hazi_macska_4_life"))
print(jelszo_erosseg("ez1feltorhetetlenjelszo"))