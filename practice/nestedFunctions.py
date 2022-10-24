def fgv1(egy_szam):
    def fgv2(szam):
        print("--- kiiratas kovetkezik ---")
        print(szam)
        print("--- kiiratas vege ---")

    if egy_szam < 20:
        fgv2(egy_szam)
    else:
        while egy_szam > 20:
            egy_szam -= 2
        else:
            fgv2(egy_szam)


fgv1(30)

####


def hatvany(kitevo):
    def n_edik_hatvany(alap):
        return alap ** kitevo
    return n_edik_hatvany

print (hatvany(2)(9))

####

def hatvany(kitevo):
    def n_edik_hatvany(alap):
        return alap ** kitevo
    return n_edik_hatvany

negyzet = hatvany(2)
harmadik = hatvany(3)
kobgyok = hatvany(1/3)

print (negyzet(2))
print (harmadik(2))
print (kobgyok(27))

####

