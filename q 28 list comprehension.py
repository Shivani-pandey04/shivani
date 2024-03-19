
a=4;b=20
n=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(a,b+1):
    n.append(i)
even = n(filter(lambda x: (x%2==0),n))
print(even)