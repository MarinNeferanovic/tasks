"""Napišite program vjezba5_zd08.py koji od korisnika traži unos cijelog broja n većeg od 1
(potrebno je napraviti provjeru), te u ovisnosti o tome je li n paran ili neparan generira i
ispisuje dvije liste: jednu koja se sastoji od n/2 neparnih prirodnih brojeva manjih ili jednakih
n, tj. [1, 3, 5, …, n (ili n-1)] i jednu od n/2 parnih prirodnih brojeva manjih ili jednakih n, tj.
[2, 4, …, n (ili n-1)] Potom treba spojiti obje liste u jednu novu listu i nju ispisati. Konačno,
dobivenu spojenu listu treba sortirati uzlazno i ispisati."""

while True:
    n = int(input("Unesite cijeli broj n većeg od 1: "))
    if n > 1:
        break
    else:
        print("Broj mora biti veći od 1. Pokušajte ponovno.")
if n % 2 == 0:
    lista1 = [i for i in range(1, n + 1, 2)]
    lista2 = [i for i in range(2, n + 1, 2)]
else:
    lista1 = [i for i in range(1, n + 1, 2)]
    lista2 = [i for i in range(2, n + 1, 2)]

spojena_lista = lista1 + lista2
spojena_lista.sort()
print("Spojena lista:", spojena_lista)