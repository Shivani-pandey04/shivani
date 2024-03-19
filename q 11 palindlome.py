num= input("enter the number")
reverse = (str(num)[::-1])
if num == reverse:
    print("the palidrome of",num,"is",reverse)
    print("the number is palindrome")
else:
    print("the number is not palidrome")