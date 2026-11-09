"""Napišite program vjezba4_zd08.py koji od korisnika traži unos proizvoljnog niza znakova (string)
te provjerava sadrži li taj niz znakova slovo 'a' (za provjeru ovog uvjeta koristite naredbu in).
Program mora ispisati odgovarajuću poruke u slučaju kada uneseni niz znakova sadrži i kada
ne sadrži slovo 'a'. zatim provjeriti koliko puta se slovo 'a' pojavljuje u unesenom nizu znakova (bez funkcije count()) te ispisati"""

s = input("Unesite proizvoljni niz znakova: ")
br = 0
for znak in s:
    if znak == 'a':
        br += 1
if 'a' in s:
    print("Uneseni niz znakova sadrži slovo 'a'.")
    print(f"Broj pojavljivanja slova 'a' u unesenom nizu znakova je: {br}")
else:
    print("Uneseni niz znakova ne sadrži slovo 'a'.")