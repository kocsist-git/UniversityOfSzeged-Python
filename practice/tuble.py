# Inmutable list

ures_tuble = ()
ures_tuble = (1,2,3)

elso_tuble = 1, 2, 3, 4
masodik_tuble = (1, 2, 3, 4, 5)
harmadik_tuble = ("gesztenye",[1,2,5], (2,4,8))

gyumi, osztalyzat, kedvencSzam = harmadik_tuble

print("gyümi:", gyumi, type(gyumi))
print("osztalyzat:", osztalyzat, type(osztalyzat))
print("Kedvanc szám::", kedvencSzam, type(kedvencSzam))

print(ures_tuble, type(ures_tuble))

# harmadik_tuble[0] = "Nem fog menni" ## Nem módosítható