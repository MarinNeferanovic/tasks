"""Napišite program vjezba5_zd07.py koji od korisnika traži unos cijelog broja n većeg od 1
(potrebno je napraviti provjeru), te generira i ispisuje listu od n prirodnih brojeva [1, 2, …, n].
Potom treba kreirati i ispisati obrnutim redoslijedom drugu listu koja također ima n
elemenata, ali sadrži samo parne prirodne brojeve [2, 4, 6, …, 2n]."""

n = int(input("Unesite cijeli broj n (veći od 1): "))
while n <= 1:
    n = int(input("Pogrešan unos. Unesite cijeli broj n (veći od 1): "))
lista1 = list(range(1, n + 1))
lista2 = list(range(2, 2 * n + 1, 2))
print(f"Prva lista: {lista1}")
print(f"Druga lista: {lista2}")
print(f"Obrnuta druga lista: {lista2[::-1]}")