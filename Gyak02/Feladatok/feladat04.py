# Készíts egy programot, ami bekér 3 számot, és a három szám alapján kiírja a felhasználónak, hogy a megadott három szám

#számtani sorozatot alkot-e,
#mértani sorozatot alkot-e,
#nem alkot sem számtani, sem mértani sorozatot!

num1=input("Add meg az elso szamot: ")
num2=input("Add meg a masodik szamot: ")
num3=input("Add meg az harmadik szamot: ")

diff = int(num2)-int(num1)
diff2 = int(num2)/int(num1)
if int(num3)-int(num2) == diff:
    print("számtani sorozatot alkot")
elif int(num3)/int(num2) == diff2:
    print("mértani sorozatot alkot")
else:
    print("nem alkot sem számtani, sem mértani sorozatot!")