#!/usr/bin/env python3
import bisect
n = int(input())
a_n = sorted(list( map(int,input().split())))
b_n1 = sorted(list( map(int,input().split())))
ans = a_n[-1]
tmp = 0
candidate = n-1
for i in range(n-1) :
    isNg = False
    tmp = bisect.bisect_right(a_n,b_n1[i])
    if tmp < i+1 :
        isNg= True
        print(-1)
        exit()
    if tmp < i+2 :
        candidate = i+1
    else :
        candidate = min(candidate,i)
print(a_n[candidate])