def koszon():
    print ("Szia!")

def koszon():
    print ("Hello!")

koszon()


#####

def koszon( nev="senki"):
    print ("Hello", nev + "!")

koszon("Tomi")
koszon()

#####

def hozzafuz (elem, lista=[]):
    lista.append(elem)
    return lista

print(hozzafuz("alma"))
print(hozzafuz("korte"))
print(hozzafuz("barack"))

#####

def hozzafuz2 (elem, lista=None):
    if lista is None:
        lista = []
    lista.append(elem)
    return lista

print(hozzafuz2("alma"))
print(hozzafuz2("korte"))
print(hozzafuz2("barack"))

####

def etkezes (ki, etel = None, ital = None):
    print (ki, "eszik")
    if etel is not None:
        print ("Amit eszik:", etel)
    if ital is not None:
        print("Amit iszik:", ital)
    print("---Jollakot---")

etkezes("Janos","rantot hus", "sor") #Számít a sorrend
etkezes("Peter","narancsle") # Sajnos ezt enni fogja
etkezes("Tomi", None, "narancsle")# Sajnos ezt is enni fogja


#### Nevesített Paraméter ####

def etkezes (ki, etel = None, ital = None):
    print (ki, "eszik")
    if etel is not None:
        print ("Amit eszik:", etel)
    if ital is not None:
        print("Amit iszik:", ital)
    print("---Jollakot---")

etkezes("Peter",ital="narancsle")
etkezes(etel="Pizza", ki="Tomi", ital="narancsle") # Így nem számít a sorrend

####