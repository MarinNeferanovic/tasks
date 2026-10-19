n = int(input("unesi broj n: "))
umnozak = 1
i = 1
while i <= n:
    if i % 2 == 1:
        umnozak *= i
    i += 1
print("Umnožak svih neparnih brojeva do", n, "je", umnozak)