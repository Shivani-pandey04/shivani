num = int(input("enter the number"))
if num >1:
    for i in range(2,num):
        if (num%i)== 0:
            print(num,"is a composite number")
            break
    else:
        print(num,"is a prime number")
else:
    print (num,"is nor prime neither composite")