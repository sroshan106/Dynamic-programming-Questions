t = int(input())
n=10**4
ugly = [0] * n 
ugly[0] = 1
i2 = i3 =i5 = 0
n2 = 2
n3 = 3
n5 = 5
for l in range(1, n): 
    ugly[l] = min(n2, n3, n5) 

    if ugly[l] == n2: 
        i2 += 1
        n2 = ugly[i2] * 2

    if ugly[l] == n3: 
        i3 += 1
        n3 = ugly[i3] * 3

    if ugly[l] == n5:  
        i5 += 1
        n5 = ugly[i5] * 5
    
for _ in range(t):
    n= int(input())
    print(ugly[n-1])
    
