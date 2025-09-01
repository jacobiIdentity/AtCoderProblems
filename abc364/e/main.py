#!/usr/bin/env python3
import bisect
n,q = map(int,input().split())
a_n = sorted(list(map(int,input().split())))
# print(a_n)
for _ in range(q) :
    b,k = map(int,input().split())
    boundL = -1
    boundR = 2*(10**8)
    cnt = 0
    mid = 0
    while boundR-boundL >1:
        mid = (boundL+boundR)//2
        indexL = bisect.bisect_left(a_n,b-mid)
        indexR = bisect.bisect_right(a_n,b+mid)
        if indexR-indexL >= k :
            boundR = mid
        else :
            boundL = mid
        cnt+=1
        # print(cnt,boundL,boundR)
    print(boundR)