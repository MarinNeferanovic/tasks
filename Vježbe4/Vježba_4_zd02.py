"""Napišite program vjezba4_zd02.py koji od korisnika traži unos duljina (float) stranica trokuta a,
b i c te prvo provjerava da li te tri stranice uopće mogu sačinjavati trokut (zbroj duljina svake
dvije stranice mora biti veći od duljine treće stranice). Ukoliko ovaj uvjet nije ispunjen ispisuje
se odgovarajuća poruka i program završava sa izvođenjem, a ukoliko je uvjet ispunjen tada se
pomoću Heronove formule računa i ispisuje površina trokuta P (koristite funkciju sqrt iz
modula math → from math import sqrt).
Heronova formula: P = √(s(s − a)(s − b)(s − c)), pri čemu je s = (a + b + c)/2"""

from math import sqrt

a = float(input("Unesite duljinu stranice trokuta a: "))
b = float(input("Unesite duljinu stranice trokuta b: "))
c = float(input("Unesite duljinu stranice trokuta c: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    P = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Površina trokuta je: {P}")
else:
    print("Stranice ne mogu sačinjavati trokut.")

