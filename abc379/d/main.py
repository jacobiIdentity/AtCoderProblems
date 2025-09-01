#!/usr/bin/env python3
import heapq
q = int(input())
trees = dict()
days = 0
for _ in range(q) :
    query = input()
    x = int(query[0])
    if x == 1 :
        if days in trees :
            trees[days] += 1
        else :
            trees[days] = 1
    if x == 2 :
        days += int(query[2:])
    if x == 3 :
        h = int(query[2:])
        # print(h,days,trees)
        tmp = list(trees.keys())
        heapq.heapify(tmp)
        ret = 0
        while tmp :
            t = heapq.heappop(tmp)
            if days-t >= h : ret += trees.pop(t)
            else :  break
        print(ret)
