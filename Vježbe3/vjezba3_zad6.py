"""program koji računa umnožak i količnik zadanih brojeva. količnik treba ispisati na dva načina: 15:4=3,75 i 15:4=3 (i ostatak 3)"""

a = int(input("Unesite prvi broj a: "))
b = int(input("Unesite drugi broj b: "))
if b == 0:
    print("Dijeljenje s nulom nije dozvoljeno.")
else:
    print("Umnožak:", a * b)
    print("Količnik:", a / b)
    print(f"Količnik: {a} : {b} = {a // b} (i ostatak {a % b})")