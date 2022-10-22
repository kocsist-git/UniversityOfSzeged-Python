# Tetszoleges szamu parameter

from multiprocessing.sharedctypes import Value


def atlag(*args):  # tuble lesz
    return sum(args) / len(args)

####


def print_info(nev, kor):
    print("Adatok", "nev:", nev, ", kor:", kor)


print_info("Tamás", 35)

adatok = ("Béla", 38)

print_info(*adatok)  # * karakter kicsomagolást végez

####

# Nevesített paraméterátadásra
# **kwargs a dupla csillag a megoldás
# **-al kibontható, csak olyan kulcsok maradhatnak, amelyik a fgv paramétereiben szerepelnek
# dictionary lesz nem tuble


def key_value(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)


key_value(nev="Kocsis Tamás", kor=35, email="tomi@random.mail")
key_value(nev="Kocsis Tamás", kor=35, kedvenc_etel=["Pizza", "Burger"])

####
# Vegyesen is használható


def key_value2(nev, **kwargs):
    print("Nev:", nev)
    for key, value in kwargs.items():
        print(key, "->", value)


key_value2("Kocsis Tamás", Beteg=True, Tanul="Igen")

####
# Indexek kiiratása egyszerűen


def fgv(*args):
    for index, value in enumerate(args):
        print(f"{index}.", value)


fgv("alma", "körte", "barack")

###


def johet_barmi(*args, **kwargs):
    for index, arg in enumerate(args):
        print(f"{index}. arg: {arg}")
    for key, value in kwargs.items():
        print(key, "->", value)

johet_barmi("alma", "körte", "barack")
print("-----")
johet_barmi(nev="Kocsis Tamás", kor=35, email="tomi@random.mail")
print("-----")
johet_barmi("alma", "körte", "barack",nev="Kocsis Tamás", kor=35, email="tomi@random.mail")

# Nevesitett, nem nevesitett parametereket nem lehet keverni

