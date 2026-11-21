zbroj_pozitivnih = 0
broj_negativnih = 0
zbroj_svih = 0
broj_unesenih = 0

while True:
    broj = int(input("Unesite cijeli broj (ili 0 za kraj unosa): "))

    if broj == 0:
        break

    zbroj_svih += broj
    broj_unesenih += 1

    if broj > 0:
        zbroj_pozitivnih += broj
    else:
        broj_negativnih += 1
        zbroj_negativnih += broj
if broj_unesenih == 0:
    print("Nije unesen niti jedan broj.")
else:
    sredina = zbroj_svih / broj_unesenih
    print(f"Zbroj pozitivnih brojeva: {zbroj_pozitivnih}")
    print(f"Broj negativnih brojeva: {broj_negativnih}")
    print(f"Sredina svih unesenih brojeva: {sredina}")