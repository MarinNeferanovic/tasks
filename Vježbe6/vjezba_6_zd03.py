"""Napišite program vjezba6_zd03.py koji od korisnika traži unos dva broja x i y te pomoću
funkcije kvadrant(x,y) provjerava i vraća redni broj kvadranta u kojem se nalazi točka (x, y).
Ukoliko se točka nalazi na nekoj od koordinatnih osi program treba vratiti naziv osi na kojoj
se nalazi zadana točka (npr. x), a u koliko se točka nalazi u ishodištu onda treba vratiti 0."""


x = float(input("Unesite x koordinatu točke: "))
y = float(input("Unesite y koordinatu točke: "))


def kvadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x == 0 and y != 0:
        return "y"
    elif y == 0 and x != 0:
        return "x"
    else:
        return 0

print(f"Točka ({x}, {y}) nalazi se u {kvadrant(x, y)} kvadrantu.")