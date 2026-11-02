"""odrediti u kojem je kvadrantu se nalazi točka s koordinatama (x, y)"""

x = float(input("Unesite x koordinatu: "))
y = float(input("Unesite y koordinatu: "))
if x > 0 and y > 0:
    print("Točka se nalazi u prvom kvadrantu.")
elif x < 0 and y > 0:
    print("Točka se nalazi u drugom kvadrantu.")
elif x < 0 and y < 0:
    print("Točka se nalazi u trećem kvadrantu.")
elif x > 0 and y < 0:
    print("Točka se nalazi u četvrtom kvadrantu.")
else:
    if x == 0 and y == 0:
        print("Točka se nalazi u ishodištu.")
    elif x == 0:
        print("Točka se nalazi na y-osi.")
    else:
        print("Točka se nalazi na x-osi.")
