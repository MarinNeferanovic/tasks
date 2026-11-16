"""Napišite program vjezba6_zd02.py koji korištenjem funkcije palindrom(s) ispituje da li je
zadani niz znakova s palindrom (jednako se čita s lijeve i desne strane). Niz znakova treba
unijeti korisnik, a program treba napraviti provjeru i vratiti odgovarajuću poruku."""

def palindrom(s):
    s = s.lower()  # Pretvaranje niza znakova u mala slova radi lakše usporedbe
    return s == s[::-1]  # Provjera je li niz znakova jednak svom obrnutom nizu

niz = input("Unesite niz znakova: ")
if palindrom(niz):
    print(f"Niz znakova '{niz}' je palindrom.")
else:
    print(f"Niz znakova '{niz}' nije palindrom.")
