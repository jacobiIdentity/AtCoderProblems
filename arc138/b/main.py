#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
flips = []
now,cnt=0,0
for i in range(n) :
    if a_n[i]!=now :
        now = 1-now
        flips.append(cnt)
        cnt = 1
    else :
        cnt += 1
if cnt > 0 :
    flips.append(cnt)
# print(flips)
if flips[0] == 0 :
    print('No')
    exit()
if len(flips) == 1 :
    print('Yes')
    exit()
if flips[0] > 1 :
    print('No')
    exit()
for i in range(len(flips)) :
    if flips[i]>1 :
        if len(flips)-1-i>1 :
            print('No')
        else :
            print('Yes')
        exit()
print('Yes')