"""Napišite program vjezba6_zd01.py koji sadrži definicije sljedećih funkcija:
a) Funkcija zbroj koja zbraja dva prirodna broja koji su ulazni parametri funkcije i vraća
vrijednost zbroja.
b) Funkcija zbroj_znamenaka koja kao ulazni parametar prima cijeli broj i vraća zbroj
njegovih znamenaka.
c) Funkcija udaljenost_od_0 koja kao ulazni parametar prima dva realna broj koji
predstavljaju x i y koordinatu neke točke u koordinatnom sustavu, te vraća
udaljenost te točke od ishodišta koordinatnog sustava (formula 𝑑 = √𝑥2 + 𝑦2).
d) Funkcija udaljenost_tocaka koja za dva uređena para (x_1, y_1) i (x_2, y_2) računa i
vraća udaljenost između točaka T_1 i T_2 zadanih pomoću ovih parova koordinata u
koordinatnom sustavu (formula 𝑑(𝑇_1, 𝑇_2) = √(𝑥_1−𝑥_2)2 + (𝑦_1 − 𝑦_2)2)."""

from math import sqrt

a=int(input("Unesite prvi prirodni broj: "))
b=int(input("Unesite drugi prirodni broj: "))
x1=float(input("Unesite x koordinatu prve točke: "))
y1=float(input("Unesite y koordinatu prve točke: "))
x2=float(input("Unesite x koordinatu druge točke: "))
y2=float(input("Unesite y koordinatu druge točke: "))
# a)
def zbroj(a, b):
    return a + b

# b)
def zbroj_znamenaka(broj):
    zbroj = 0
    while broj > 0:
        zbroj += broj % 10
        broj //= 10
    return zbroj

# c)
def udaljenost_od_0(x, y):
    return sqrt(x**2 + y**2)

# d)
def udaljenost_tocaka(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f"Zbroj dva prirodna broja {a} i {b} je: {zbroj(a, b)}")
print(f"Zbroj znamenaka broja {a} je: {zbroj_znamenaka(a)}")
print(f"Zbroj znamenaka broja {b} je: {zbroj_znamenaka(b)}")
print(f"Udaljenost točke ({x1}, {y1}) od ishodišta koordinatnog sustava je: {udaljenost_od_0(x1, y1)}")
print(f"Udaljenost između točaka ({x1}, {y1}) i ({x2}, {y2}) je: {udaljenost_tocaka(x1, y1, x2, y2)}")