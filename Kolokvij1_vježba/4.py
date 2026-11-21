n=int(input("Unesite pozitivan cijeli broj: "))

while n <= 0:
    n=int(input("broj mora biti veći od 0: "))

    dijelitelj = 1
    broj_djeljitelja = 0

    print("dijeljitelji broja" , n, "su: ")

    while dijelitelj <= n:
        if n % dijelitelj == 0:
            print(dijelitelj, end=" ")
            broj_djeljitelja += 1
        dijelitelj += 1