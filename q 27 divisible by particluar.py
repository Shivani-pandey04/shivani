"""list=int(input("12,52,40,82,94,5,31,22"))

result = list(filter(lambda x : (x % 2 == 0) ,list))
print("number that are divisible by 2 are: " ,result)"""



list=[]
num =int(input("enter the no of list: "))
for i in range(num):
    ele = int(input("enter no: "))
    list.append(ele)

div = int(input("enter the no with which divibility needs to check:"))
for j in range(num):
    print()
if ele%div == 0:
    print("the number is divisible.")
#else:
    #print("the number is not divisble.")