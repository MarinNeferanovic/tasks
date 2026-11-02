"""Napišite program vjezba4_zd05.py koji od korisnika traži unos koeficijenata kvadratne
jednadžbe a, b i c (kvadratna jednadžba ax² + bx + c = 0) i potom ispisuje dva rješenja ove
kvadratne jednadžbe x1 i x2 ukoliko je diskriminanta D > 0, jedinstveno rješenje x ukoliko je D =
0 ili ispisati da nema realnih rješenja ukoliko je D < 0 (diskriminanta D = b² − 4ac). Ukoliko je a =
0 program samo treba ispisati odgovarajuću pogrešku ('Ovo nije kvadratna jednadžba') i završiti
sa izvođenjem (koristite modul math"""

from math import *

a = float(input("Unesite koeficijent a: "))
if a == 0:
    print("Ovo nije kvadratna jednadžba.")
    exit()
b = float(input("Unesite koeficijent b: "))
c = float(input("Unesite koeficijent c: "))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b+sqrt(D))/(2*a)
    x2 = (-b-sqrt(D))/(2*a)
    print(f"Rješenja su: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Jedinstveno rješenje je: x = {x}")
else:
    print("Nema realnih rješenja.")