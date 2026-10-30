"""za zadanu duljinu u centimetrima ispisuje odgovarajuću duljunu u stopama i inčama (npr. 178 cm = 5 stopa i 10 inča)"""

cm = float(input("Unesite duljinu u centimetrima: "))
inches = cm / 2.54
feet = int(inches // 12)
inches = int(inches % 12)
print(f"{cm} cm = {feet} stopa i {inches} inča")