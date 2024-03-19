print("enter the number of terms:", end="")
tot = int(input())

anoms = lambda x: 2**x
print()
for i in range(tot):
    print("2 raised to the power",i,"is",anoms(i))