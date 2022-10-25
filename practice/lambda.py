from ast import arg


osszead = lambda x, y: x + y
print(osszead(1,2))

osszead2 = lambda *args: sum(args)
print(osszead2(1,2,3,5))

szavak = ["sor", "karacsonyfa", "to", "ajandek", "gesztenyekocka"]
rendezett = sorted(szavak, key=lambda szo: len(szo))
print(rendezett)

szavak.sort(key=lambda szo: szo[-1])
print(szavak)