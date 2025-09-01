#!/usr/bin/env python3
from collections import defaultdict
import heapq
n = int(input())
q = int(input())
boxToCards = {j:[] for j in range(1,n+1)}
cardToBoxs = dict()
cardToBoxsSet = defaultdict(set)
for _ in range(q) :
    op,*ij = map(int,input().split())
    if op==1 :
        i,j = ij[0],ij[1]
        if len(boxToCards[j])== 0 :
            heapq.heapify(boxToCards[j])
        heapq.heappush(boxToCards[j],i)
        if i not in cardToBoxsSet :
            cardToBoxs[i] = []
            heapq.heapify(cardToBoxs[i])
        if j not in cardToBoxsSet[i] :
            cardToBoxsSet[i].add(j)
            heapq.heappush(cardToBoxs[i],j)
        cardToBoxsSet[i].add(j)
    elif op==2 :
        i = ij[0]
        # print(*boxToCards[i])
        tmp = []
        while boxToCards[i] :
            tmp.append(heapq.heappop(boxToCards[i]))
        print(*tmp)
        # print(' '.join(tmp))
        while tmp :
            heapq.heappush(boxToCards[i],tmp.pop())
    else :
        j = ij[0]
        # print(*cardToBoxs[j])
        tmp = []
        while cardToBoxs[j] :
            tmp.append(heapq.heappop(cardToBoxs[j]))
        print(*tmp)
        # print(' '.join(tmp))
        while tmp :
            heapq.heappush(cardToBoxs[j],tmp.pop())
    # print(boxToCards)
    # print(cardToBoxs)
    # print(cardToBoxsSet)