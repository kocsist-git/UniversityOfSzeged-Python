# 6. feladat: Szóbeli vizsga (3 pont)
# A kedvenc tantárgyunkból a szóbeli vizsga a következőképpen zajlik: 
# egyszerre bemegy valamennyi hallgató egy terembe, és sorban helyet foglalnak a 
# teremben lévő, 1-től kezdődően sorszámozott székeken. 
# A teremben pontosan annyi szék van, mint ahány hallgató vizsgázik. 
# Az oktató a vizsgán kiválaszt egy adott sorszámú széken ülő hallgatót, 
# feltesz neki egy kérdést, majd ezután az 1-gyel nagyobb sorszámú széken ülő hallgatótól kérdez. 
# A legutolsó széken ülő hallgató után az első széken ülő hallgatóval folytatódik a sor. 
# Az oktató utolsó kérdése mindig egy egyszerűbb "bónusz kérdés".

# Írj Python szkriptet, amely beolvas 3 egész számot: rendre a vizsgázó hallgatók számát, 
# az oktató által feltett kérdések számát és azon hallgató székének sorszámát, 
# aki az első kérdést kapja! A szkript írja ki a konzolra, 
# hogy hányas széken ülő hallgató fogja kapni az utolsó, "bónusz" kérdést! 
# Hibakezeléssel nem kell foglalkoznod, feltesszük, hogy az input minden esetben helyes.

# Példa:

# Vizsgazok szama: 5
# Feltett kerdesek szama: 8
# Az elso kerdest kapo hallgato szekszama: 2

# A(z) 4. szeken ulo hallgato kapja a bonusz kerdest.
# Vizsgazok szama: 10
# Feltett kerdesek szama: 22
# Az elso kerdest kapo hallgato szekszama: 5

# A(z) 6. szeken ulo hallgato kapja a bonusz kerdest.

vizsgazok = int(input("Vizsgazok szama: "))
kerdesek = int(input("Feltett kerdesek szama: "))
elsoKszek = int(input("Az elso kerdest kapo hallgato: "))

szek = elsoKszek

for i in range(kerdesek - 1):
    if szek + 1 > vizsgazok:
        szek = 1
    else:
        szek+=1

print(f"A(z) {szek}. szeken ulo hallgato kapja a bonusz kerdest.")
