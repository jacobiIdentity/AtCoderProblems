#!/usr/bin/env python3
n = int(input())
a_n =list( map(int,input().split()))
l1 = a_n
while len(l1)>2 :
    tmp = []
    for i in range(len(l1)//2) :
        tmp.append(max(l1[2*i],l1[2*i+1]))
    l1 = tmp
print(a_n.index(min(l1))+1)
