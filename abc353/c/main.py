#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
a_n.sort()
right = n-1
k = 10**8
ans = (n-1)*sum(a_n)
for i in range(n-1) :
    while right > -1 :
        if a_n[i]+a_n[right] >= k :
            right -= 1
        else :
            break
    # print(i,right)
    ans -= (n-max(i,right)-1)*k
print(ans)
