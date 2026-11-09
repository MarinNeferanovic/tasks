"""Napišite program vjezba5_zd05.py koji od korisnika traži unos niza znakova (string), te
potom ispisuje taj niz znakova bez praznina i pretvara sva slova u velika slova (npr. za unos
'progra mi rANje ' ispisuje 'PROGRAMIRANJE')."""

s = input("Unesite proizvoljni niz znakova: ")
s = s.replace(" ", "")
s = s.upper()
print(s)