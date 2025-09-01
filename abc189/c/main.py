#!/usr/bin/env python3
import heapq
n = int(input())
a_n = list(map(int,input().split()))
q = []
heapq.heapify(q)
ans = 0
for i in range(n) :
    if i == 0 :
        heapq.heappush(q,(-a_n[i],i))
        continue
    a,j = heapq.heappop(q)
    # print(i,a,j)
    if a_n[i] < -a :
        tmp = j
        # print(i,j,-a*(i-j))
        ans = max(ans,-a*(i-j))
        while q :
            a,j = heapq.heappop(q)
            if a_n[i] < -a :
                ans = max(ans,-a*(i-j))
                # print(i,j,-a*(i-j))
                tmp = min(tmp,j)
            else :
                heapq.heappush(q,(a,j))
                break
        heapq.heappush(q,(-a_n[i],tmp))
        
    else :
        heapq.heappush(q,(a,j))
        heapq.heappush(q,(-a_n[i],i))
# print(q)
while q :
    a,j = heapq.heappop(q)
    # print(j,n,-a*(n-j))
    ans = max(ans,-a*(n-j))
print(ans)
