"""Napišite program vjezba4_zd08.py koji od korisnika traži unos proizvoljnog niza znakova (string)
te provjerava sadrži li taj niz znakova slovo 'a' (za provjeru ovog uvjeta koristite naredbu in).
Program mora ispisati odgovarajuću poruke u slučaju kada uneseni niz znakova sadrži i kada
ne sadrži slovo 'a'"""

s = input("Unesite proizvoljni niz znakova: ")
if 'a' in s:
    print("Uneseni niz znakova sadrži slovo 'a'.")
else:
    print("Uneseni niz znakova ne sadrži slovo 'a'.")
