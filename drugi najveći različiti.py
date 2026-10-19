n = int(input("Unesite N: "))

if n < 1:
    print("N mora biti barem 1.")
else:
    x = int(input("Unesite prvi broj: "))
    najveci = x
    drugi = x
    postojiDrugi = False
    i = 2

    while i <= n:
        x = int(input("Unesite broj: "))

        if x > najveci:
            drugi = najveci
            najveci = x
            postojiDrugi = True
        elif x < najveci:
            if not postojiDrugi or x > drugi:
                drugi = x
                postojiDrugi = True

        i += 1

    if postojiDrugi:
        print("Drugi najveći različiti broj je:", drugi)
    else:
        print("Ne postoji drugi različiti broj.")
