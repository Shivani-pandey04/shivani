list=[]
num =int(input("enter the no of list: "))
for i in range(num):
    ele = int(input("enter no: "))
    list.append(ele)
print("largest element in list:",max(list))
print("smallest element in list",min(list))