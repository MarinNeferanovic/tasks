"""Napišite program vjezba5_zd06.py koji od korisnika traži unos dvaju nizova znakova niz_1 i
niz_2. Ukoliko se niz znakova niz_1 pojavljuje u nizu niz_2 program ispisuje sve znakove u
nizu niz_2 nakon prvog pojavljivanja zadanog niza niz_1 (bez da ispiše prvo pojavljivanje niza
niz_1), a u protivnom ispisuje odgovarajuću poruku."""

niz_1 = input("Unesite prvi niz znakova: ")
niz_2 = input("Unesite drugi niz znakova: ")
if niz_1 in niz_2:
    pocetak = niz_2.index(niz_1) + len(niz_1)
    print(niz_2[pocetak:])
else:
    print(f"niz_1 se ne nalazi u nizu znakova {niz_2}.")