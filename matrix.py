x=[[1,2,3],
  [7,8,9]]
y=[[9,8,7],
   [0,9,8]]
result=[[0,0,0],
       [0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[j][k]
for r in result:
    print(r)
