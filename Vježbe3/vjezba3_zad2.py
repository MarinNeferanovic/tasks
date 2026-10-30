"""dva zadana broja a i b (0<b<100) ispisuje njihobu sumu, razliku, umnožak,kvocijent, cijelobrojni kvocijent, potenciju a na b, i ostatak pri cijelobrojnom dijeljenu a i b."""
a=int(input("Unesite prvi broj a: "))
b=int(input("Unesite drugi broj b: "))
if b <= 0 or b >= 100:
    print("Drugi broj b mora biti veći od 0 i manji od 100.")
else:
    print("Suma:", a + b)
    print("Razlika:", a - b)
    print("Umnožak:", a * b)
    print("Kvocijent:", a / b)
    print("Cijelobrojni kvocijent:", a // b)
    print("Potencija a na b:", a ** b)
    print("Ostatak pri cijelobrojnom dijeljenju a i b:", a % b)