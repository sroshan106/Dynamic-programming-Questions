def compute(n,k):
    l=[]
    for i in range(n+1):
        l.append([0]*(n+1))
    l[0]=[1]*(n+1)
    for i in range(1,n+1):
        l[i][0]=1
        for j in range(1,i+1):
            if i==j:
                l[i][j]=1
            else:
                l[i][j]=l[i-1][j-1]+l[i-1][j]
    return l[n][k]

n = int(input())
k = int(input())
result = compute(n,k)
print(result)
