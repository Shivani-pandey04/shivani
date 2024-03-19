#to find the sum of digits of given number
num=input("enter the number")
sum= 0
for i in num:
    sum = sum + int(i)
print ("the sum of digit is:" ,sum)