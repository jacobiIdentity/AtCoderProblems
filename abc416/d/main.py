#!/usr/bin/env python3
import heapq
t = int(input())
for _ in range(t) :
    n,m = map(int,input().split())
    a_n = list(map(int,input().split()))
    b_n = sorted(list(map(int,input().split())),reverse=True)
    heapq.heapify(a_n)
    ans = sum(a_n)+sum(b_n)
    cnt = 0
    for i in range(n) :    
        if len(a_n)==0 :
            break
        moreN = False
        while a_n :
            a = heapq.heappop(a_n)
            if b_n[i]+a>=m :
                moreN = True
                break
        if moreN :
            cnt += 1
    ans -= cnt*m
    print(ans)
