#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
for i in range(n) :
    a_set = set(a_n)
    if len(a_set&set(range(1,m+1)))==m :
        a_n.pop()
    else :
        print(i)
        exit()
print(n)