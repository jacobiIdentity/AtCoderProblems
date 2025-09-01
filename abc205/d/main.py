#!/usr/bin/env python3
import bisect
n,q = map(int,input().split())
a_n = list(map(int,input().split()))
a_set = set(a_n)
for _ in range(q) :
    k = int(input())
    ng,ok = 0,10**19
    mid = 0
    while ok-ng>1 :
        mid = (ok+ng)//2
        pos = bisect.bisect_right(a_n,mid)
        # print(ok,ng,mid,pos)
        if mid-pos < k :
            ng = mid
        elif mid - pos > k :
            ok = mid
        else :
            while mid in a_set :
                mid -= 1
            break
    print(mid)
