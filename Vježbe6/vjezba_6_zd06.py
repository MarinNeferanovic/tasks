"""Napišite program vjezba6_zd06.py koji računa ukupan iznos narudžbe u internetskoj trgovini. Program
treba sadržavati sljedeće funkcije:
a) Funkcija cijena_stavke(cijena, kolicina) prima jediničnu cijenu proizvoda i naručenu količinu te vraća
ukupan iznos za taj proizvod.
b) Funkcija primijeni_popust(iznos, postotak) prima iznos i postotak popusta te vraća iznos umanjen za
zadani popust.
c) Funkcija trosak_dostave(iznos) vraća trošak dostave prema iznosu narudžbe nakon primjene popusta.
Dostava je besplatna za iznose od najmanje 50 EUR, a u ostalim slučajevima iznosi 4 EUR.
d) Funkcija main() od korisnika traži unos cijene i količine za tri različita proizvoda te postotka popusta
na cijelu narudžbu. Korištenjem prethodno definiranih funkcija treba izračunati i ispisati:
iznos narudžbe prije popusta,
iznos narudžbe nakon popusta,
trošak dostave,
konačan iznos za plaćanje.
Sve novčane iznose ispišite na dvije decimale. Pretpostavite da korisnik unosi ispravne podatke.
Primjer: Za proizvode čije su cijene i količine redom (10, 2), (15, 1) i (5, 3), iznos prije popusta je 50 EUR.
Uz popust od 10 %, iznos nakon popusta je 45 EUR, dostava iznosi 4 EUR, a konačan iznos za plaćanje je
49 EUR."""





def main():
    u_cijena = 0
    for i in range(3):
        cijena = float(input(f"Unesite cijenu proizvoda {i + 1}: "))
        kolicina = int(input(f"Unesite količinu proizvoda {i + 1}: "))
        u_cijena += cijena_stavke(cijena, kolicina)

    p_popust = float(input("Unesite postotak popusta na cijelu narudžbu: "))

    inp = primijeni_popust(u_cijena, p_popust)
    dostava = trosak_dostave(inp)
    konacan_iznos = inp + dostava

    print(f"Iznos narudžbe prije popusta: {u_cijena:.2f} EUR")
    print(f"Iznos narudžbe nakon popusta: {inp:.2f} EUR")
    print(f"Trošak dostave: {dostava:.2f} EUR")
    print(f"Konačan iznos za plaćanje: {konacan_iznos:.2f} EUR")

def cijena_stavke(cijena, kolicina):
    return cijena * kolicina

def primijeni_popust(iznos, postotak):
    return iznos * (1 - postotak / 100)

def trosak_dostave(iznos):
    if iznos >= 50:
        return 0
    else:
        return 4


if __name__ == "__main__":
    main()