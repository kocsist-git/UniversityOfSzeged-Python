def hello(nev):
    print("Hello " + nev + "!")

hello("Béla")

# A kesobb definialt fuggveny felulirja a regebbit
# nem lehet eltero parameter listaval tobbet definialni


def hello2(nev="Senki"): # default parameterek megadasa
    print("Hello " + nev + "!")

hello2()     
hello2("Béla")

def osszead(a, b=0, c=0):
    return a + b + c

print(osszead(5))               # 5 + 0 + 0
print(osszead(5, 2))            # 5 + 2 + 0
print(osszead(5, 2, 3))         # 5 + 2 + 3

def info(felhasznalonev, jelszo=None, szak=None): # Nevesitett parameterek
    if jelszo is not None:      # ha megadtuk a jelszo paramétert...
        print(felhasznalonev, "jelszava:", jelszo)
    if szak is not None:        # ha megadtuk a szak paramétert...
        print(felhasznalonev, "szakja:", szak)

info("Károly", szak="proginfó", jelszo="sdfsdf") # nevesített paraméterátadás
