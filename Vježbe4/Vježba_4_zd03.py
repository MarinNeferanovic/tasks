"""Napišite program vjezba4_zd03.py koji od korisnika traži unos dva cijela broja a i b, te unos
računske operacije (+, -, * ili /), te u ovisnosti od unesene računske operacije vraća
zbroj/razliku/umnožak/kvocijent brojeva a i b. Ukoliko korisnik ne unese ispravnu računsku
operaciju program mora ispisati odgovarajuću poruku o grešci i završiti sa izvođenjem."""

o = input("Unesite računsku operaciju (+, -, * ili /): ")
a = int(input("Unesite prvi cijeli broj a: "))
b = int(input("Unesite drugi cijeli broj b: "))

if o == "+":
    print(f"Zbroj brojeva {a} i {b} je: {a + b}")
elif o == "-":
    print(f"Razlika brojeva {a} i {b} je: {a - b}")
elif o == "*":
    print(f"Umnožak brojeva {a} i {b} je: {a * b}")
elif o == "/":
    if b != 0:
        print(f"Kvocijent brojeva {a} i {b} je: {a / b}")
    else:
        print("Greška: Dijeljenje s nulom nije dozvoljeno.")
else:
    print("Greška: Niste unijeli ispravnu računsku operaciju.")