"""Napišite program koji za zadani broj (koji sami zadajemo) ispisuje:
a) cjelobrojnu vrijednost int
b) u obliku pomočnog broja float
c) cjelobrojnu vrijednost (int) u binarnom, oktalnom i heksadecimalnom obliku
d) pridruženu logičku vrijednost bool (True ili False)
e) reprezentaciju u obliku stringa (str)"""

a=input("Unesite broj: ")
# a)
print("Cjelobrojna vrijednost (int):", int(a))
# b)
print("U obliku pomočnog broja float:", float(a))
# c)
print("U binarnom obliku:", bin(int(a)))
print("U oktalnom obliku:", oct(int(a)))
print("U heksadecimalnom obliku:", hex(int(a)))
# d)
print("Logička vrijednost (bool):", bool(a))
# e)
print("Reprezentacija u obliku stringa (str):", str(a))