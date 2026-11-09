"""Napišite program vjezba5_zd03.py koji od korisnika traži unos niza znakova (string) te unos
jednog cijelog broja n, a potom provjerava nalazi li se broj n+1 u zadanom nizu znakova."""
s = input("Unesite proizvoljni niz znakova: ")
n = int(input("Unesite cijeli broj n: "))

if str(n + 1) in s:
    print(f"Broj {n + 1} se nalazi u nizu znakova.")
else:
    print(f"Broj {n + 1} se ne nalazi u nizu znakova.")