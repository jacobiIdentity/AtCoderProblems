#!/usr/bin/env python3
n = int(input())
cnts = [0]*(n+1)
for i in range(1,n) :
    iCnt = 0
    tmp = 1
    while tmp * tmp < i+1 :
        if i%tmp == 0 :
            iCnt += 1 if tmp*tmp == i else 2
        tmp += 1
    cnts[i] = iCnt
ans = 0
for i in range(1,n+1) :
    ans += cnts[i]*cnts[n-i]
print(ans)