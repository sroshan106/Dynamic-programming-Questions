def compute(n):
    l=[]
    for i in range(n+1):
        l.append([0]*(n+1))
    l[0][0]=1
    for i in range(1,n+1):
        l[i][0] = l[i-1][i-1]
        for j in range(1,i+1):
            l[i][j]=l[i][j-1]+l[i-1][j-1]

    return l[n-1][j-1]
n = int(input())
result = compute(n)

print(result)
