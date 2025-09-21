#!/usr/bin/env python3
import heapq
n,k = map(int,input().split())
a_n,b_n,c_n = [],[],[]
for _ in range(n) :
    a,b,c = map(int,input().split())
    a_n.append(a)
    b_n.append(b)
    c_n.append(c)
ans = [0]*n
i = 0 
restaurant = []
peopleCnt = 0
now = 0
while i<n :
    while peopleCnt+c_n[i]> k and restaurant :
        t,j = heapq.heappop(restaurant)
        now = max(now,t)
        peopleCnt -= c_n[j]
    peopleCnt += c_n[i]
    now = max(now,a_n[i])
    heapq.heappush(restaurant,(now+b_n[i],i))
    ans[i] = now
    i+=1
print(*ans,sep='\n')
