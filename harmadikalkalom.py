# nyelvi szerkezetek
import random

def ker_ter(alap, magassag):
    k = 2 * alap + 2 * magassag
    t = alap * magassag
    return k, t


felhasznalo_kora = int(input('Hány éves vagy?: '))

if felhasznalo_kora <= 18:
    print("gyerek")
elif felhasznalo_kora <= 25:
    print("Ifjú")
elif felhasznalo_kora <= 65:
    print("koros")
else:
    print("nyugger")

uzenet = "Gyere be" if felhasznalo_kora >= 18 else "maradj kint"
print(uzenet)

i = 1

while i < 10:
    print(i)

    if i == 5:
        break
    else:
        print("gond nélkül lefutott!")

    i += 1

print("vége a ciklusnak")

alap = 3
magassag = 4

eredmeny = ker_ter(alap, magassag)
print(f"Kerület = {eredmeny[0]}, Terület = {eredmeny[1]}")

i = 0
while i < 5:
    print(random.randint(1, 90))
    i += 1