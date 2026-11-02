"""Napišite program vjezba4_zd07.py koji od korisnika traži unos dviju varijabli argument i baza
(varijable moraju biti tipa float) koje predstavljaju argument i bazu logaritma
(log_baza(argument)). Program prvo mora provjeriti jesu li unesene vrijednosti ispravne u
smislu definicije funkcije logaritma (argument mora biti strogo veći od 0, a baza logaritma mora
biti strogo veća od 0 i različita od 1) te ukoliko jesu ispisuje vrijednost logaritma sa zadanom
bazom i argumentom (koristite funkciju log(x, base) koja se nalazi u modulu math)"""

from math import log

a = float(input("Unesite argument logaritma: "))
b = float(input("Unesite bazu logaritma: "))

if a <= 0 or b <= 0 or b == 1:
    print("Greška: Unesene vrijednosti nisu ispravne za definiciju logaritma.")
else:
    result = log(a, b)
    print(f"Vrijednost logaritma log_{b}({a}) je: {result}")