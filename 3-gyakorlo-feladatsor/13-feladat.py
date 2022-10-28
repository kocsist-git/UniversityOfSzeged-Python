# 13. feladat: Fájlok csoportosítása (5 pont)
# Krisztián szeretne statisztikát készíteni a Dokumentumok mappájában található fájlokról, 
# ezért egy Python szkriptet ír. A szkript feladata, hogy megszámolja, 
# hogy az adott mappán belül mennyi található a különböző kiterjesztésekből. 
# A program egy részét Krisztián már megírta, viszont a statisztika-készítésben kellene neki egy kis segítség.
# 
# Írj egy statisztika nevű függvényt, amely egy listát kap paraméterül! 
# A lista fájlok neveit tartalmazza, kiterjesztéssel együtt. 
# A fájlnévben a kiterjesztés alatt a legutolsó pont karakter után lévő szöveget értjük.
# A függvény számolja meg, hogy az egyes kiterjesztések hányszor fordulnak elő a listában,
# és az eredményt adja vissza egy dictionary-ben, a példában látható formátumban!
# 
# A feladatot úgy oldd meg, hogy a kiterjesztés vizsgálata során ne különböztesd meg a kis- és nagybetűket 
# (tehát pl. hello.py és WORLD.PY egyaránt py kiterjesztésűek).
# 
# Példa:
# 
# Input: ['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY', 'biro.gib.maxpont.py', 'russian-driving-fails.mp4']
# Return: {'py': 3, 'java': 1, 'mp4': 2}

def statisztika(fajlok):
    eredmeny = dict()

    for file in fajlok:
        kiterjesztes = file.split(".")[-1].lower()
        if kiterjesztes not in eredmeny:
            eredmeny[kiterjesztes] = 1
        else:
            eredmeny[kiterjesztes] += 1

    return eredmeny
print(statisztika(['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY', 'biro.gib.maxpont.py', 'russian-driving-fails.mp4']))