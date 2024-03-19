'''l = [1,2,0,41,0,82,12,2,42,6,75,41,1]
print("the og list is:"+str(l))
l= l(set(l))
print("the list after removing duplicate:"+str(l))'''


def function(x):
    return list(dict.fromkeys(x))
list = function(["20","42","45","20","50","85","12"])
print(list)