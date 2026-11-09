"""Napišite program vjezba5_zd10.py koji od korisnika traži unos pet imena te ih sortira po
abecedi, a potom ispisuje svako ime u svom retku sa odgovarajućim rednim brojem ispred
imena."""
imena = []
for i in range(5):
    ime = input(f"Unesite {i+1}. ime: ")
    imena.append(ime.lowercase())  # Pretvaranje imena u mala slova radi pravilnog sortiranja

imena.sort()
for i, ime in enumerate(imena, start=1):
    print(f"{i}. {ime}")