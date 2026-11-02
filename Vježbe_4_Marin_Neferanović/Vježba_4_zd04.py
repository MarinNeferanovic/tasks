"""Napišite program vjezba4_zd04.py koji od korisnika traži unos broja bodova postignutih na
ispitu (mora biti broj između 0 i 100, u protivnom program ispisuje odgovarajuću poruku i
prekida se izvođenje) te vraća pripadnu ocjenu"""

b = int(input("Unesite broj bodova postignutih na ispitu (0-100): "))
if b < 0 or b > 100:
    print("Broj bodova mora biti između 0 i 100.")
    exit()
if b >= 0 and b <= 60:
    print("Ocjena je 1 (nedovoljan).")
elif b <= 70:
    print("Ocjena je 2 (dovoljan).")
elif b <= 80:
    print("Ocjena je 3 (dobar).")
elif b <= 90:
    print("Ocjena je 4 (vrlo dobar).")
else:
    print("Ocjena je 5 (odličan).")