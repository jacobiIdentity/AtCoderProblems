#!/usr/bin/env python3
n = int(input())
ans = 0
k = 1
while k*k < 2*n+1 :
    if (2*n)%k == 0 and ((2*n)//k+1-k)%2 == 0 :
        ans += 1
        # print(k)
    if (2*n)%(2*n//k) == 0 and ((2*n)//(2*n//k)+1-(2*n//k))%2 == 0 :
        ans += 1
        # print(n//k)
    k+=1
print(ans)