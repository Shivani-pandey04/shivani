#palidrome using function
num = input("enter the number")
try:
    val= int(num)
    if num==str(num)[::-1]:
        print("palidrome")
    else:
        print ("not palidrome")
except ValueError:
    print("Invalid choice")
    
