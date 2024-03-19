terms=int(input("enter the number foe fibonacci series:"))
f = 0
s = 1
count = 0
if terms<=0:
    print("INVAILD")
elif terms == 1:
    print("fibonacci series upto",terms)
    print(f)
else:
    print("fibonacci series")
    while count< terms:
        print(f)
        n=f+s
        f=s
        s=n
        count +=1