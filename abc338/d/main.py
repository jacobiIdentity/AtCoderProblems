#!/usr/bin/env python3
n, m = map(int,input().split())
x_n = list(map(int,input().split()))
ans = 10**8
for i in range(n) :
    tmp = 0
    for j in range(m-1) :
        p,q = min(x_n[j],x_n[j+1]),max(x_n[j],x_n[j+1])
        if p<= i+1 and i+1 < q :
            tmp += n -(q-p)
        else :
            tmp += (q-p)
    ans = min(tmp, ans)
print(ans)