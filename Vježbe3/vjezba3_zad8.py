"""Napišite program vjezba3_zd8.py koji za tri zadane različite znamenke a, b i c ispisuje sve troznamenkaste brojeve koji se mogu napisati kombinacijom tih znamenaka.
Brojeve ispišite u dva stupca, tako da u istom retku budu brojevi s istom znamenkom stotica,
odvojeni jednim tabulatorom. Pretpostavite da su a, b i c različiti od nule. Primjer traženog oblika
ispisa:
abc acb
bac bca
cab cba"""

# jednostavniji način rješavanja je da samo varijable izrazimo u programu kao što zapravo i jest zadatak.
# a=1
# b=2
# c=3
# print(a+b+c, a+c+b)
# print(b+a+c, b+c+a)
# print(c+a+b, c+b+a)

a = input("Unesite prvu znamenku: ")
b = input("Unesite drugu znamenku: ")
c = input("Unesite treću znamenku: ")
if (len(a) != 1 or len(b) != 1 or len(c) != 1
        or not a.isdigit() or not b.isdigit() or not c.isdigit()):
    print("Unesene vrijednosti nisu jednoznamenkaste!")
elif a == "0" or b == "0" or c == "0":
    print("Niti jedna varijabla ne smije biti jednaka nuli!")
elif a == b or a == c or b == c:
    print("Znamenke moraju biti različite!")
else:
    print(a + b + c, a + c + b)
    print(b + a + c, b + c + a)
    print(c + a + b, c + b + a)