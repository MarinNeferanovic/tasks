a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))
c = int(input("Unesite treći broj:"))

if a <= b and a <= c:
    print("Najmanji broj je:", a)
elif b <= a and b <= c:
    print("Najmanji broj je:", b)
else:
    print("Najmanji broj je:", c)