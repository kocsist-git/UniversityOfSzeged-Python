# 12. feladat: Kurzuskódok (5 pont)
# Informatikus szakon többféle kurzust is felvehetünk. 
# Az informatikával kapcsolatos tárgyak kurzuskódja I betűvel, a matekos tárgyak kurzuskódja M betűvel,
# míg a szabadon választható tárgyak kurzuskódja X betűvel kezdődik.
# 
# Írj egy kurzuskodot_csoportosit nevű függvényt, amely egy olyan szöveget kap paraméterül, 
# ami pontosvesszővel elválasztott kurzuskódokat tartalmaz! A függvény csoportosítsa a 
# szövegben szereplő kurzuskódokat "infós", "matekos" és "szabvál" kategóriákba, 
# majd adja vissza az így kapott csoportosítást egy dictionary-ben, a példában látható formátumban!
# Ha a paraméterben kapott érték az üres string, akkor a függvény egy üres dictionary-vel térjen vissza!
# 
# Példa:
# 
# Input: 'IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E'
# Return: {'infos': ['IB370G', 'IB370E'], 'matekos': ['MBNXK114E', 'MBNXK114G'], 'szabval': ['XA0021-GTK-MM1']}
# 
# Input: 'ITN714G;IB402g;XN0011-01317;IB202g'
# Return: {'infos': ['ITN714G', 'IB402g', 'IB202g'], 'matekos': [], 'szabval': ['XN0011-01317']}
# 
# Input: ''
# Return: {}

def kurzuskodot_csoportosit(kodok):
    if kodok == "": return dict()

    lista = kodok.split(";")
    eredmeny = {
        "infos":list(),
        "matekos":list(),
        "szabval":list()
    }
    for kurzus in lista:
        if kurzus[0] == "I": eredmeny["infos"].append(kurzus)
        if kurzus[0] == "M": eredmeny["matekos"].append(kurzus)
        if kurzus[0] == "X": eredmeny["szabval"].append(kurzus)

    return eredmeny

print(kurzuskodot_csoportosit('IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E'))
print(kurzuskodot_csoportosit('ITN714G;IB402g;XN0011-01317;IB202g'))
print(kurzuskodot_csoportosit(''))

