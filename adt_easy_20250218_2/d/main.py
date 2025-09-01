#!/usr/bin/env python3
n,q = map(int,input().split())
cnt = [0]*n
for _ in range(q) :
    i,x = map(int,input().split())
    if i == 1 :
        cnt[x-1] += 1
    elif i == 2 :
        cnt[x-1] += 2
    else :
        print('Yes' if cnt[x-1]>=2 else 'No')
        