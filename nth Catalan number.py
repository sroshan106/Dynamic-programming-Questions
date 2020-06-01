def compute(n):
    t=n+1
    if n<=1:
        return 1
    catalan=[0]*t
    catalan[0]=1
    catalan[1]=1
    for i in range(2, n + 1): 
        catalan[i] = 0
        for j in range(i): 
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n] 

n = int(input())
result = compute(n-2)
print(result)
