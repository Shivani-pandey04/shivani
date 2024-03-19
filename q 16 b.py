#pattern 2
rows = int(input("enter the no of rows:"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end= " ")
    print()
    #print((rows-i)*" "+i * "*")