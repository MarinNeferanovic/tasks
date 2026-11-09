"""Napišite program vjezba5_zd02.py koji od korisnika traži unos dva niza znakova (string) te
provjerava nalazi li se prvi niz znakova negdje unutar drugog i ispisuje odgovarajuću poruku."""

s1 = input("Unesite prvi niz znakova: ")
s2 = input("Unesite drugi niz znakova: ")

if s1 in s2:
    print(f"Niz '{s1}' se nalazi unutar niza '{s2}'.")
else:
    print(f"Niz '{s1}' se ne nalazi unutar niza '{s2}'.")