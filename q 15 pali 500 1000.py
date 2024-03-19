min= int(input("enter the value "))
max= int(input("enter the value "))
print("palidrome no between %d and %d are: " %(min,max))  
for num in range(min,max +1):
    temp = num
    reverse = 0
    
    while(temp>0):
        rem= temp% 10
        reverse = (reverse*10)+rem
        temp=  temp//10
    
    if(num==reverse):
        print("%d" %num, end=" ")
        

    