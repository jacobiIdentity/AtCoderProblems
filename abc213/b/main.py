#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
pos1, pos2 = a_n.index(max(a_n[0:2])),a_n.index(min(a_n[0:2]))
for i in range(2,n) :
    if a_n[i] > a_n[pos1] :
        pos1, pos2 = i, pos1
        # print(pos1, pos2)
    elif a_n[pos2] < a_n[i] and a_n[i] < a_n[pos1] :
        pos2 = i
        # print(pos1, pos2)
print(pos2+1)