# 4. feladat: Négyzetgyök (3 pont)
# Írj Python szkriptet, amely beolvas a standard bemenetről egy egész számot,
# és kiírja annak a négyzetgyökét! Amennyiben a beolvasott szám negatív,
# akkor a Negativ szambol nem vonunk negyzetgyokot! szöveget írasd ki!

# Példa:

# Adj meg egy szamot: 2
# A beirt szam negyzetgyoke: 1.4142135623730951
# Adj meg egy szamot: -1
# Negativ szambol nem vonunk negyzetgyokot!

num = int(input("Adj meg egy szamot: "))

if (num<0):
    print("Negativ szambol nem vonunk negyzetgyokot!")
else:
    print("A beirt szam negyzetgyoke:",num**0.5)