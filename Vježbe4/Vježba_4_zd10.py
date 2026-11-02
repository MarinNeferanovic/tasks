"""Napišite program vjezba4_zd10.py koji od korisnika traži unos niza znakova (string) duljine 5
(npr. 'kapak'), pri čemu svaki znak prilikom unosa pohranjuje u zasebnu varijablu (resp. a, b, c,
d i e), te potom provjerava tvori li uneseni niz znakova palindrom (riječ koja se jednako čita s
lijeva na desno i s desna na lijevo). Pokušajte zadatak riješiti tako da samo jednom koristite
funkciju input(). Program na kraju treba ispisati adrese memorijskih lokacija varijabli a, b, c, d i
e u kojima su pohranjeni znakovi (koristite funkciju id() za dohvaćanje adrese memorijske
lokacije varijable)"""

s = input("Unesite niz znakova duljine 5: ")
if len(s) != 5:
    print("Greška: Niz znakova mora biti duljine 5.")
else:
    a, b, c, d, e = s[0], s[1], s[2], s[3], s[4]
    if a == e and b == d:
        print("Uneseni niz znakova tvori palindrom.")
    else:
        print("Uneseni niz znakova ne tvori palindrom.")
    
    print(f"Adresa memorijske lokacije varijable a: {id(a)}")
    print(f"Adresa memorijske lokacije varijable b: {id(b)}")
    print(f"Adresa memorijske lokacije varijable c: {id(c)}")
    print(f"Adresa memorijske lokacije varijable d: {id(d)}")
    print(f"Adresa memorijske lokacije varijable e: {id(e)}")