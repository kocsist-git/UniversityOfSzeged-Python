# 4. feladat: Discord emote-ok (3 pont)
# Discordon lehetőségünk van különféle emote-okkal reagálni üzenetekre. 
# Az emote-ok között megtalálhatók például az angol ábécé betűi A-tól Z-ig.
# Márk ezeknek az emote-oknak a használatával szeretne kirakni egy szót, viszont fontos tudni, 
# hogy a Discord minden emote-ot csak egyszer enged felhasználni!

# Írj egy kirakhato nevű függvényt, amely egyetlen szót (string) kap paraméterül, 
# és visszaadja, hogy az kirakható-e úgy, hogy minden betűt csak egyszer használunk fel! 
# A kis- és nagybetűket ne különböztessük meg!

# Tipp: Érdemes először csupa kisbetűssé (vagy csupa nagybetűssé) alakítani a szót, 
# így például a második példában látható Alma szóban ismétlődő betűként kezeljük az a betűt.

# Példa:

# Input: 'Szilva'
# Return: True

# Input: 'Alma'
# Return: False

# Input: 'Gorogdinnye'
# Return: False

def kirakhato(szo):
    szo = szo.lower()
    betuk = set(szo)
    return True if len(szo) == len(betuk) else False

print(kirakhato("Alma"))
print(kirakhato("Szilva"))
print(kirakhato("Gorogdinnye"))
