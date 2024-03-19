#sum of n no using function
def sumofN(k):
    s=0
    for i in range(1,k+1):
        s += i
    return s
print("enter the value of n",end="")
try:
    n= int(input())
    if n< 0:
        print("\n Invalid Input!")
    else:
        sum= sumofN(n)
        print("\nSum =",sum)
except ValueError:
    print("\nInvalid Input!")