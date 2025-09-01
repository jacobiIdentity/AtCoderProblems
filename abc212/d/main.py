#!/usr/bin/env python3
import heapq
q = int(input())

que = []
heapq.heapify(que)
tmp = 0
for _ in range(q) :
    query = input()
    if query[0] == '1' : 
        heapq.heappush(que,int(query[2:])-tmp)
    elif query[0] == '2' : 
        tmp += int(query[2:])
    else :
        print(heapq.heappop(que)+tmp)
    
