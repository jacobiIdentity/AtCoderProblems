#!/usr/bin/env python3
n = int(input())
L_i = list(map(int,input().split()))
canOpen = set()
canOpen.add(0)
for i in range(n) :
    if L_i[i] :
        break
    canOpen.add(i+1)
canOpen.add(n)
for i in reversed(range(n)) :
    if L_i[i] :
        break
    canOpen.add(i)
print(n+1-len(canOpen))
