# 3. feladat: Béla (2 pont)
# Béla egy online játékkal játszik. A játékban talált egy bugot, amit kihasználva 
# többször is be tud lépni a játékba ugyanazzal a felhasználónévvel.
# A játékostársai ezt nem tartják tisztességesnek, ezért úgy döntenek, hogy Bélát kirúgják a játékból.

# Írj egy belat_kirug nevű függvényt, amely egy listát kap paraméterül, ami a játékosok neveit tartalmazza (stringek).
# A függvény távolítsa el a listából az EpicBela20 játékosnév összes előfordulását, majd térjen vissza az így kapott listával!

# Példa:

# Input: ['EpicBela20', 'python4life', 'EpicBela20', 'EpicBela20', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']
# Return: ['python4life', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']

def belat_kirug(lista):
    while lista.count("EpicBela20") > 0:
        lista.remove("EpicBela20")
    return lista


print(belat_kirug(['EpicBela20', 'python4life', 'EpicBela20', 'EpicBela20', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']))