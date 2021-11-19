bilA = int(input("Masukan bilangan a : "))
bilB = int(input("Masukan bilangan b : "))
bilC = int(input("Masukan bilangan c : "))

print("a = ", bilA)
print("b = ", bilB)
print("c = ", bilC)

if bilA > bilB and bilA > bilC:
    maks = bilA
    print("Bilangan terbesar adalah a = ", maks)
elif bilB > bilA and bilB > bilC:
    maks = bilB
    print("Bilangan terbesar adalah b = ", maks)
else:
    maks = bilC
    print("Bilangan terbesar adalah c = ", maks)
