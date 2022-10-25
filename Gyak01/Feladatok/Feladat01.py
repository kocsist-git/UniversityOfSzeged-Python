# 1. Írj egy programot, ami bekéri a felhasználó adatait változóban, majd soronként kiírja azt!

from errno import EMLINK


name = input("Mi a neved? ")
email = input("Email címed? ")
fav = input("Kedvenc jatekod? ")
age = input("Hány éves vagy? ")

print("Szia",name)
print("Email cimed:",email)
print("Kedvenc játékod?:",fav)
print("Korod:",age)

