"""Napišite program vjezba6_zd05.py koji sadrži funkcije unos_int() i prost(n), te koji sadrži
glavnu funkciju main(). Funkcija unos_int() mora od korisnika tražiti unos cijelog broja i kao
povratnu vrijednost vraćati unos korisnika konvertiran u cjelobrojni tip (int). Funkcija prost(n)
mora imati jedan ulazni parametar n za koji mora vršiti provjeru da li je prost ili složen, te u
ovisnosti o tome vraćati logičku vrijednost True ili False. Funkcija main() nema ulaznih
parametara niti povratne vrijednosti, a u tijelu funkcije main() uporabom funkcija unos_int() i
prost(n) mora se od korisnika tražiti unos cijelog broja te izvršiti provjeru je li uneseni broj
prost ili složen i u skladu s time ispisati odgovarajuću poruku."""

def unos_int():
    return int(input("Unesite cijeli broj: "))

def prost(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    user_input = unos_int()
    if prost(user_input):
        print(f"Broj {user_input} je prost.")
    else:
        print(f"Broj {user_input} nije prost.")

main()

