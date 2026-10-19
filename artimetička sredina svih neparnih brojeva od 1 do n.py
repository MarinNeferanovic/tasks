n=int(input("unesi broj n: "))
if n>=1 and n%2!=0:
    suma=0
    for i in range(1,n+1):
        suma+=i
    aritmeticka_sredina=suma/n
    print("Aritmetička sredina svih brojeva od 1 do", n, "je:", aritmeticka_sredina)
else:
    print("broj je pozitivan")