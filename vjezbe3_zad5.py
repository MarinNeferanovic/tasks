"""program koji za zadano vrijeme u sekundama (vrijeme mora biti cijeli broj) ispisuje odgovarajuće vrijednosti u danima, satima, minutama i sekundama (npr. 100000 sekundi = 1 dan, 3 sata, 46 minuta i 40 sekundi)"""
s = int(input("Unesite vrijeme u sekundama: "))
days = s // 86400
s %= 86400
hours = s // 3600
s %= 3600
minutes = s // 60
s %= 60
seconds = s
print(f"{days} dana, {hours} sati, {minutes} minuta i {seconds} sekundi")