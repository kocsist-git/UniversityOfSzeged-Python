# 5. feladat: Armstrong-szám (4 pont)
# A matematikában egy n-jegyű számot Armstrong-számnak nevezünk, 
# ha minden számjegyét az n-edik hatványra emelve és összeadva az eredeti számot kapjuk. 
# Például a 153 egy Armstrong-szám, hiszen .

# Írj egy armstrong_szam nevű függvényt, amely garantáltan egy 
# nemnegatív egész számot kap paraméterül, és visszaadja, hogy a
# paraméterben kapott szám Armstrong-szám vagy sem!

# Példa:

# Input: 153
# Return: True

# Input: 1999
# Return: False

# Input: 8208
# Return: True

def armstrong_szam (szam):
    osszeg = 0
    for szam_jegy in str(szam):
        osszeg += int(szam_jegy) ** len(str(szam))
    
    return True if osszeg == szam else False 

print(armstrong_szam(153))
print(armstrong_szam(1999))
print(armstrong_szam(8208))