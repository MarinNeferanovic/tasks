"""Napišite program vjezba5_zd04.py koji od korisnika traži unos niza znakova (string) te potom
ispisuje svaki treći znak u tom nizu znakova, pri čemu svaka dva znaka u tom ispisu moraju
biti razdvojena prazninom (' '), ali bez vodećih i završnih praznina (npr. za unos
'otorinolaringologija' program treba ispisati 'o r o r g o j')."""



S=input("Unesite proizvoljni niz znakova: ")
treći=S[0::3]
print(" ".join(treći))