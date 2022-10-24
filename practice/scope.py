def fgv():
    # Eléri a string változót.
    print(string)


# Global Scoop
string = "Cool"
fgv()

#####


def fgv2():
    string2 = "Hello local"  # Név elfedés problémája, a lokálisan létrehozott változók mindig megszünnek a block után.
    print(string2)


string2 = "Cool2"
fgv2()
print(string2)

#####


def fgv3():
    print(string3)
    # string3 = "Hiba lesz itt", mert a függvény Scope kesöbb hozzuk létre a változót, mint ahogy használnánk
    print(string3)


string3 = "Cool3"
fgv3()

#####


def fgv4():
    global string3
    print(string3)
    # után már nincs hiba, mert eggyártelmű az értelmezőnek a feladat.
    string3 = "global használata"
    print(string3)


string3 = "Cool4"
fgv4()


#####