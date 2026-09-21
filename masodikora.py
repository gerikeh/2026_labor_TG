# Ez a második labor feladatait tartalmazza
felhasznalo_kora = int(15.65)
felhasznalo_kora = int(input("Hány éves vagy: "))
felhasznalo_kora += 1
felhasznalo_neve = input('Kérem a nevet:')
felhasznalo_neve *= 2
metszet = felhasznalo_neve[:-5]
jegyek = [2, 5, 4, 3]
jegyek += [5]
del jegyek[0]
halmaz = {'magyar', 'angol', 'orosz', 3}
hallgato = {"nev": 'Jolán', "kor": 19}
print(hallgato["nev"])
print(halmaz)
print('Szia', felhasznalo_neve, "!", jegyek)


print('Jó', 'reggelt', 'DUE', end='\n\n' , sep='-')
print('Több soros\n'
'kiiras\n'
      '!!!!!!!!')

print(f'Szia {felhasznalo_neve}! {jegyek}')
print(f'kora: {felhasznalo_kora: 30}')

