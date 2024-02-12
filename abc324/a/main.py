#!/usr/bin/env python3
n = int(input())
an = list(map(int, input().split()))
isYes = True
a0 = an[0]
for i in range(n) :
    if a0 != an[i] :
        print('No')
        exit()
print('Yes')