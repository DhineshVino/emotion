##a=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
##b=[[2,2,2,2],[2,2,2,2],[2,2,2,2]]
##c=[[0,0,0],[0,0,0],[0,0,0]]
##if len(a[0])==len(b):
##    for i in range(len(a[0])):
##        for j in range(len(a[0])):
##            c[i][j]=a[i][j]*b[i][j]
##else:
##    print("matrix cannot be multiply")
##for s in c:
##    print(c)
##    
# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
