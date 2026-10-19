n = int(input("unesi broj n: "))
zbroj = 0
i = 1
while i <= n:
    if i % 2 == 0:
        zbroj += i
    i += 1
print("Zbroj svih parnih brojeva do", n, "je", zbroj)