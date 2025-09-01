#!/usr/bin/env python3
import heapq
n,w = map(int,input().split())
d = dict()
notEmptyX = set()
for i in range(n) :
    x,y = map(int,input().split())
    if x not in d :
        d[x] = []
        heapq.heapify(d[x])
        notEmptyX.add(x)
    heapq.heappush(d[x],(y,i+1))
# print(d)
deleteTime = {i+1:float('inf') for i in range(n)}
now = 0
while len(d) == w :
    tmp = 0
    delSet = set()
    delKeySet = set()
    for dd in d :
        minDD,i = heapq.heappop(d[dd])
        tmp = max(tmp,minDD)
        delSet.add(i)
        if len(d[dd]) == 0 :
            delKeySet.add(dd)
    for dd in delKeySet :
        d.pop(dd)
    for dd in delSet :
        deleteTime[dd] = tmp
q = int(input())
for _ in range(q) :
    t,a = map(int,input().split())
    print('Yes' if deleteTime[a]>t else 'No')
    
