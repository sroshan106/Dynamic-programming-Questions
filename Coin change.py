def compute(coins,m,n):
    mat = [0]*(n+1)
    mat[0]=1
    for i in range(m):
        for j in range(coins[i],n+1):
            mat[j]+=mat[j-coins[i]]
    return mat[n]

coins =[1,2,5]
m= len(coins)
n = int(input())
print(compute(coins,m,n))
