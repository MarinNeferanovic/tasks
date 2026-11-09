""" Napišite program vjezba5_zd01.py koji od korisnika traži unos niza znakova (string), te za
zadani niz znakova ispisuje sljedeće:
a) njegovu duljinu
b) najveći (max) element u tom nizu
c) najmanji (min) element u tom nizu
d) drugi znak u tom nizu (što ako je niz kraći od dva znaka?)
e) zadnji znak u tom nizu
f) tri puta zaredom ispisuje čitav niz, a između pojedinih ispisa stavlja točku (.)
(npr. za niz znakova 'Ovo je niz' ispisuje 'Ovo je niz.Ovo je niz.Ovo je niz')
g) ispisuje zadani niz bez prvog i zadnjeg znaka (što ako je duljina niza manja od 2?)
h) ispisuje zadani niz obrnutim redoslijedom (npr. za 'abcd' ispisuje 'dcba')
i) ispisuje svako drugo slovo u zadanom nizu (npr. za 'abcd' ispisuje 'bd')
j) sadrži li zadani niz slovo 'a' i ako ga sadrži, na kojoj se poziciji u nizu prvi put
pojavljuje slovo 'a', a ako ga ne sadrži onda ispisuje odgovarajuću poruku. """

s = input("Unesite proizvoljni niz znakova: ")
# a) duljina niza
print(f"Duljina niza znakova je: {len(s)}")
# b) najveći element u nizu
print(f"Najveći element u nizu je: {max(s)}")
# c) najmanji element u nizu
print(f"Najmanji element u nizu je: {min(s)}")
# d) drugi znak u nizu
if len(s) >= 2:
    print(f"Drugi znak u nizu je: {s[1]}")
else:
    print("Niz je kraći od dva znaka.")
# e) zadnji znak u nizu
print(f"Zadnji znak u nizu je: {s[-1]}")
print(f"Tri puta zaredom ispisani niz s točkom između: {s}.{s}.{s}")
if len(s) >= 2:
    print(f"Niz bez prvog i zadnjeg znaka: {s[1:-1]}")
else:
    print("Duljina niza je manja od 2.")
# g) ispisuje zadani niz bez prvog i zadnjeg znaka
print(f"Niz bez prvog i zadnjeg znaka: {s[1:-1]}")
# h) ispisuje zadani niz obrnutim redoslijedom
print(f"Niz obrnutim redoslijedom: {s[::-1]}")
# i) ispisuje svako drugo slovo u zadanom nizu
print(f"Svako drugo slovo u nizu: {s[1::2]}")
# j) sadrži li zadani niz slovo 'a' i ako ga sadrži, na kojoj se poziciji u nizu prvi put pojavljuje slovo 'a', a ako ga ne sadrži onda ispisuje odgovarajuću poruku.
if 'a' in s:
    print(f"Slovo 'a' se pojavljuje prvi put na poziciji: {s.index('a')}")
else:
    print("Slovo 'a' se ne pojavljuje u nizu.")