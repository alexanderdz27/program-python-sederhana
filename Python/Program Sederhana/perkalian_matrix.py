
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[1,1,1],
    [1,1,1],
    [1,1,1]]

hasil = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           hasil[i][j] += X[i][k] / Y[k][j]

for l in hasil:
   print(l)