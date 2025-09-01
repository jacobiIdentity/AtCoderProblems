#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
# print(a_n)
ans = float('inf')
sumA = sum(a_n)
for i in range(1,1<<n-1) :
    iStr = ('{:0'+str(n)+'b}').format(i )
    tmp = 0
    for j in range(n) :
        if iStr[j] == '1' :
            tmp += a_n[j]
    ans = min(ans,max(tmp,sumA-tmp))
    
print(ans)