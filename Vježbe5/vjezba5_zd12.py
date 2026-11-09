"""Napišite program vjezba5_zd12.py koji od korisnika traži unos nekog niza znamenaka (npr.
'3412301230') te potom računa aritmetičku sredinu svih unesenih znamenaka."""

n = input("Unesite niz znamenaka: ")
z = [int(z) for z in n]
ar = sum(z) / len(z)
print(f"Aritmetička sredina unesenih znamenaka je: {ar}")