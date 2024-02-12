from collections import defaultdict
n, m = map(int, input().split())
a_ij = [list(map(int, input().split())) for _ in range(m)]
fDict = defaultdict(set)
for i in range(m) :
    for j in range(n-1) :
        fDict[a_ij[i][j]].add(a_ij[i][j+1])
        fDict[a_ij[i][j+1]].add(a_ij[i][j])
ans = n*(n-1)
for i in range(1,n+1) :
    ans -= len(fDict[i])
print(ans//2)