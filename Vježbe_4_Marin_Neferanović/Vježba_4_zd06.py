"""Napišite program vjezba4_zd06.py koji konvertira dekadski cijeli broj u binarni, oktalni ili
heksadecimalni oblik, tj. od korisnika traži unos cijelog broja (int) te unos baze u kojoj će se taj
broj ispisati (2, 8 ili 16), a potom u ovisnosti od odabrane baze ispisuje zadani broj u
odgovarajućoj bazi. Ukoliko baza nije ispravno zadana program treba ispisati odgovarajuću
poruku o grešci"""

b = int(input("Unesite cijeli broj: "))
base = int(input("Unesite bazu (2, 8 ili 16): "))
if base == 2:
    print(f"Broj {b} u binarnom obliku je: {bin(b)}")
elif base == 8:
    print(f"Broj {b} u oktalnom obliku je: {oct(b)}")
elif base == 16:
    print(f"Broj {b} u heksadecimalnom obliku je: {hex(b)}")
else:
    print("Greška: Niste unijeli ispravnu bazu.")