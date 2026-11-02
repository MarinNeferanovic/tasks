unos_a = int(input("Unesite početak intervala A: "))
unos_b = int(input("Unesite kraj intervala B: "))

if unos_a > unos_b:
    unos_a, unos_b = unos_b, unos_a

brojac = 0
zbroj = 0
broj = unos_a

while broj <= unos_b:
    broj_djelitelja = 0
    djelitelj = 1

    while djelitelj <= broj:
        if broj % djelitelj == 0:
            broj_djelitelja += 1
        djelitelj += 1

    if broj_djelitelja == 2:
        print(broj)
        brojac += 1
        zbroj += broj

    broj += 1

print("Broj prostih brojeva:", brojac)
print("Zbroj prostih brojeva:", zbroj)