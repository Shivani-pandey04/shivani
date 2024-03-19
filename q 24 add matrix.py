x = [[23,50,12],
     [5,8,71,],
     [87,24,49]]

y = [[40,50,72,],
     [7,86,48],
     [15,83,43]]

r = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j] = x[i][j] + y[i][j]
print("addition is:")
        
for r in r:
    
    print(r)