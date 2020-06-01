def compute(n,k):
    result =1
    if k ==n:
        return 1
    if k>n:
        return 0
    for i in range(n,n-k,-1):
        result*=i
    return result
n = int(input())
k = int(input())
result = compute(n,k)
print(result)
