d ={}
def compute(n):
    result= 0
    if n<=2:
        return n
    if n in d:
        return d[n]
    result = compute(n-1)+(n-1)*compute(n-2)
    if n not in d:
        d[n]=result
    return result

n = int(input())
print(compute(n))
