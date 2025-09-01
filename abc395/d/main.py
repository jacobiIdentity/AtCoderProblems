#!/usr/bin/env python3
from collections import defaultdict
n,q = map(int,input().split())
# nest = defaultdict(set)
p = [i for i in range(n+1)]
swap1 = [i for i in range(n+1)]
swap2 = [i for i in range(n+1)]
# for i in range(1,n+1) :
#     nest[i].add(i)
for _ in range(q) :
    op = list(map(int,input().split()))
    if op[0] == 1 :
        # nest[p[op[1]]].discard(op[1])
        # nest[swap2[op[2]]].add(op[1])
        p[op[1]] = swap2[op[2]] 
    elif op[0] == 2 :
        swap1[swap2[op[1]]],swap1[swap2[op[2]] ],swap2[op[1]],swap2[op[2]]=op[2],op[1],swap2[op[2]],swap2[op[1]]
    else :
        print(swap1[p[op[1]]])
    # print(p)
    # print(nest)
    # print(swap1)
    # print(swap2+)