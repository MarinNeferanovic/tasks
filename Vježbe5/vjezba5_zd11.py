"""Napišite program vjezba5_zd11.py koji od korisnika traži unos niza znakova koji se sastoji od
proizvoljne kombinacije slova A, B i C (npr. 'CCBAAABACBBBCACCCCACBBBA') te potom vraća
udio (postotak) pojavljivanja pojedinog slova u ovom nizu. Također, na kraju ispišite uneseni
niz znakova sortiran po abecedi"""

niz = input("Unesite niz znakova koji se sastoji od slova A, B i C: ")
broj_A = niz.count('A')
broj_B = niz.count('B')
broj_C = niz.count('C')

ukupno = len(niz)
p_A = (broj_A / ukupno) * 100
p_B = (broj_B / ukupno) * 100
p_C = (broj_C / ukupno) * 100

print(f"Postotak pojavljivanja slova A: {p_A:.2f}%")
print(f"Postotak pojavljivanja slova B: {p_B:.2f}%")
print(f"Postotak pojavljivanja slova C: {p_C:.2f}%")

sortirani_niz = ''.join(sorted(niz))
print(f"Sortirani niz znakova: {sortirani_niz}")