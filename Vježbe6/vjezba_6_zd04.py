"""Napišite program vjezba6_zd04.py koji korištenjem rekurzivne funkcije
binarno_pretrazivanje(l,s) traži element s u sortiranoj listi brojeva l. Binarno pretraživanje
niza (binary search) traži element u sortiranoj listi na način da ga uspoređuje sa srednjim
elementom u listi i ako je srednji element veći od zadanog onda se uzima lijeva polovica liste i
ponavlja se poziv funkcije na toj polovici, a u protivnom se uzima desna polovica liste.
Postupak se ponavlja rekurzivno sve dok se ne pronađe zadani element u listi, ili dok se ne
iscrpi lista. Funkcija vraća True ili False u ovisnosti o tome je li zadani element pronađen ili
nije."""

l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
s = int(input("Unesite element koji želite pronaći u listi: "))

def binarno_pretrazivanje(l, s):
    if len(l) == 0:
        return False
    srednji_index = len(l) // 2
    srednji_element = l[srednji_index]
    
    if srednji_element == s:
        return True
    elif srednji_element > s:
        return binarno_pretrazivanje(l[:srednji_index], s)
    else:
        return binarno_pretrazivanje(l[srednji_index + 1:], s)

if binarno_pretrazivanje(l, s):
    print(f"Element {s} je pronađen u listi.")
else:
    print(f"Element {s} nije pronađen u listi.")
