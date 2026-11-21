n=int(input("Unesite pozitivan cijeli broj: "))
brojac = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 != 0:
        brojac += 1

        for znamenka in str(i):
            zbroj_znamenaki += int(znamenka)

        zbroj_znamenaki = 0

        if zbroj_znamenaki % 2 == 0:
            print(i)
            brojac += 1
print(f"Broj pronađenih brojeva: {brojac}")
