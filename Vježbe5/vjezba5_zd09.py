"""Napišite program vjezba5_zd09.py koji od korisnika traži unos proizvoljnog niza znakova
(string) te od tog niza znakova generira listu. Potom broji koliko se puta u listi pojavljuje
praznina ' ' i taj podatak ispisuje. Nakon toga listu sortira uzlazno i iz nje izbacuje posljednji
element te je još jednom ispisuje. Konačno, ukoliko se u listi pojavljuje slovo 'a' (treba
provjeriti) onda izbacuje prvo pojavljivanje tog slova iz liste i ponovno ispisuje listu."""

niz = input("Unesite proizvoljni niz znakova: ")
lista = list(niz)
bp = lista.count(' ')
print("Broj pojavljivanja praznine: ", bp)

lista.sort()
print("Sortirana lista: ", lista)

lista.pop()
print("Lista nakon izbacivanja posljednjeg elementa: ", lista)

if 'a' in lista:
    lista.remove('a')
    print("Lista nakon izbacivanja prvog pojavljivanja slova 'a': ", lista)

# Ako ne želimo ispisati razmake u listi, nova lista (uz pomoć ai-a)
# lista_za_ispis = [znak for znak in lista if znak != ' ']
# print("Lista bez razmaka: ", lista_za_ispis)
# Originalna lista i dalje sadrži razmake, pa ih možemo ispravno prebrojiti
# pomoću lista.count(' '). Broj razmaka zato ne treba mijenjati s bp - 1.