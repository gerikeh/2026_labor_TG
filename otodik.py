# OOP


class Auto:
    kerekek = 4

    def __init__(self, marka, tipus="nincs"):
        self.marka = marka
        self.tipus = tipus


class Teglalap:
    szog = 90

    def __init__(self, a_oldal=5, b_oldal=10):
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def terulet(self):
        return self.a_oldal * self.b_oldal

    def kerulet(self):
        return self.a_oldal * 2 + self.b_oldal * 2


# Téglalap

t = Teglalap()

print(t.a_oldal, t.b_oldal)
print(t.terulet())
print(t.kerulet())


# Autó

a1 = Auto("Peugeot")
a2 = Auto(marka="Chery", tipus="Tiggo")

# a1.kerekek = 3

print(a1.kerekek, a2.kerekek, Auto.kerekek)
print(a1.marka, a1.tipus)
print(a2.marka, a2.tipus)


# Dolgozó

class Dolgozo:
    def __init__(self, nev, kor, email):
        self.nev = nev
        self.email = email

        hiba = True

        for i in range(len(str(kor))):
            if str(kor)[i].isnumeric():
                hiba = False
                break

        if hiba:
            print("Nem szamjegyeket adtal meg")
            self.kor = 0
        else:
            self.kor = kor

    def korkerdes(self):
        return self.kor


d = Dolgozo("Józsi", 34, "jozsi@g.hu")

print(d.nev)
print(d.kor)
print(d.email)
print(d.korkerdes())
