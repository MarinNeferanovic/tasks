"""Napišite program vjezba4_zd09.py koji od korisnika traži unos jednog slova engleske abecede
te potom ispisuje radi li se o velikom (A-Z) ili o malom slovu (a-z), a nakon toga ispisuje
odgovarajući ASCII kod pridružen tom slovu (koristite funkciju ord() pomoću koje se dohvaća
vrijednost znaka zapisana u ASCII kodnom sustavu). Ukoliko unos nije slovo engleske abecede
program treba ispisati odgovarajuću poruku o grešci (koristite modul string)"""

import string

a = input("Unesite jedno slovo engleske abecede: ")
if len(a) != 1 or a not in string.ascii_letters:
    print("Greška: Niste unijeli jedno slovo engleske abecede.")
else:
    if a.isupper():
        print("Uneseno slovo je veliko.")
    else:
        print("Uneseno slovo je malo.")
    print(f"ASCII kod unesenog slova: {ord(a)}")