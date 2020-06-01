def getMaxGold(gold,m,n):
    l=[]
    for _ in range(m+2):
        l.append([0]*n)
    for i in range(m):
        l[i+1][0]=gold[i][0]
    maxx=0
    for i in range(1,n):
        for j in range(1,m+1):
            l[j][i]=gold[j-1][i]+max(l[j-1][i-1],l[j][i-1],l[j+1][i-1])
            if maxx<l[j][i]:
                maxx=l[j][i]
    return maxx
gold = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]] 
  
m = 4
n = 4
  
print(getMaxGold(gold, m, n)) 
