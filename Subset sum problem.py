def compute(l,n,summ):
    mat =[]
    for _ in range(n+1):
        mat.append([0]*(summ+1))
    
    for i in range(summ+1):
        mat[0][i]=0

    for i in range(n+1):
        mat[i][0]=1

    for i in range(1,n+1):
        for j in range(1,summ+1):
            if j < l[i-1]:
                mat[i][j]=mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j] or mat[i-1][j-l[i-1]]
            
    return mat[n][summ]==1

l=list(map(int,input().split(" ")))
n= len(l)
summ = int(input())
print(compute(l,n,summ))
