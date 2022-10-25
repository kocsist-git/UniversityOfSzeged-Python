# változó létrehozása és értékadás
# Pythonban egy változó akkor jön létre, amikor először értéket adunk neki.

az_en_valtozom = "valami szöveg"        

# A változónév csak betűket, számokat és alulvonás karaktert (_) tartalmazhat.
# A változónév csak betűvel vagy alulvonással kezdődhet (nem kezdődhet számmal).
# A változónév tartalmazhat ékezeteket, azonban ezt célszerű kerülni.
# A változónév érzékeny a kis- és nagybetűkre (tehát pl. foo, Foo és FOO három különböző változónak számít).
# A változónév természetesen nem lehet foglalt kulcsszó (pl.: class, except stb.).

desszert = "palacsinta"
Desszert = "tiramisu"

print(desszert)         # a változónév kis- és nagybetűérzékeny!
print(Desszert)


# Dinamikusan típusosság
val = 42     
val = 12.345 
val = "sajt" 

val = "Ez egy szöveg"
print(type(val)) # milyen típusú adatot tárol, egyszerűen lekérdezhetjük a type() függvény segítségével.


